package main

import (
	"fmt"
	"log"
	"os"
	"time"

	"github.com/joho/godotenv"
	"gopkg.in/telegram-bot-api.v4"
)

func main() {
	// Load environment variables
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}

	// Get telegram bot token and chat ID
	botToken := os.Getenv("TELEGRAM_BOT_TOKEN")
	chatID := os.Getenv("TELEGRAM_CHAT_ID")

	// Create a new telegram bot API client
	bot, err := tgbotapi.NewBotAPI(botToken)
	if err != nil {
		log.Fatal(err)
	}

	// Get odoo instance URL
	odooURL := os.Getenv("ODOO_URL")

	// Set up a timer to run the backup job every 24 hours
	ticker := time.NewTicker(24 * time.Hour)
	for range ticker.C {
		// Execute a curl command to back up the odoo instance
		output, err := exec.Command("curl", "-X", "POST", odooURL + "/web/database/backup", "-d", "token=" + os.Getenv("ODOO_TOKEN")).Output()
		if err != nil {
			// Send a message through telegram if there was an error
			msg := tgbotapi.NewMessage(chatID, "Error backing up odoo instance: "+err.Error())
			bot.Send(msg)
		} else {
			// Send a message through telegram if the backup was successful
			msg := tgbotapi.NewMessage(chatID, "Odoo instance successfully backed up. Output: "+string(output))
			bot.Send(msg)
		}
	}
}
