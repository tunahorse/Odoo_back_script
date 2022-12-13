package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
)

func main() {
	// Set the database name and the path to save the backup file
	dbName := "my_odoo_db"
	backupPath := "/path/to/save/odoo_db_backup.dump"

	// Create a new file to save the backup to
	file, err := os.Create(backupPath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Use the "pg_dump" command to create the backup
	cmd := exec.Command("pg_dump", dbName)
	cmd.Stdout = file

	// Run the command and check for errors
	err = cmd.Run()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Odoo database backup created successfully!")
}
