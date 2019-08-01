ZOOM_ROOM_ALERT = {
  "type": "object",
  "properties": {
    "event": {
      "type": "string"
    },
    "payload": {
      "type": "object",
      "properties": {
        "account_id": {
          "type": "string"
        },
        "object": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "room_name": {
              "type": "string"
            },
            "calendar_name": {
              "type": "string"
            },
            "email": {
              "type": "string"
            },
            "issue": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}