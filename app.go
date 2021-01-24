package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

func health(w http.ResponseWriter, r *http.Request) {
	var data = map[string]interface{}{
		"message": "is running..",
	}

	response, _ := json.Marshal(data)

	fmt.Println(response)
	w.Write(response)
}

func main() {
	http.HandleFunc("/", health)
	http.ListenAndServe(":8991", nil)
}
