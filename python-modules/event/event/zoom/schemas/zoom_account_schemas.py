ACCOUNT_CREATED = {
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
          "operator": {
            "type": "string"
          },
          "object": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              },
              "owner_id": {
                "type": "string"
              },
              "owner_email": {
                "type": "string"
              }
            }
          }
        }
      }
    }
}

ACCOUNT_DISASSOCIATED = {
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
        "operator": {
          "type": "string"
        },
        "object": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "owner_id": {
              "type": "string"
            },
            "owner_email": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}

ACCOUNT_UPDATED = {
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
        "operator": {
          "type": "string"
        },
        "object": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "account_name": {
              "type": "string"
            },
            "account_alias": {
              "type": "string"
            },
            "account_support_name": {
              "type": "string"
            },
            "account_support_email": {
              "type": "string"
            },
            "managed_domains": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        },
        "old_object": {
          "type": "object",
          "properties": {
            "$changed_field_name": {
              "type": "string"
            }
          }
        },
        "operation": {
          "type": "string"
        }
      }
    }
  }
}

ACCOUNT_SETTINGS_UPDATED = {
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
        "operator": {
          "type": "string"
        },
        "object": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "account_name": {
              "type": "string"
            },
            "account_alias": {
              "type": "string"
            },
            "account_support_name": {
              "type": "string"
            },
            "account_support_email": {
              "type": "string"
            },
            "managed_domains": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          }
        },
        "old_object": {
          "type": "object",
          "properties": {
            "$changed_field_name": {
              "type": "string"
            }
          }
        },
        "operation": {
          "type": "string"
        }
      }
    }
  }
}