USER_CREATED = {
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
        "creation_type": {
          "type": "string"
        },
        "object": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "email": {
              "type": "string"
            },
            "type": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}

USER_UPDATED = {
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
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "phone_number": {
              "type": "string"
            },
            "phone_country": {
              "type": "string"
            },
            "company": {
              "type": "string"
            },
            "pmi": {
              "type": "string"
            },
            "use_pmi": {
              "type": "string"
            },
            "pic_url": {
              "type": "string"
            },
            "vanity_name": {
              "type": "string"
            },
            "email": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "language": {
              "type": "string"
            },
            "host_key": {
              "type": "string"
            },
            "role": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "dept": {
              "type": "string"
            },
            "settings": {
              "type": "object",
              "properties": {
                "feature": {
                  "type": "object",
                  "properties": {
                    "meeting_capacity": {
                      "type": "string"
                    },
                    "large_meeting": {
                      "type": "string"
                    },
                    "large_meeting_capacity": {
                      "type": "string"
                    },
                    "webinar": {
                      "type": "string"
                    },
                    "webinar_capacity": {
                      "type": "string"
                    }
                  }
                }
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

USER_SETTINGS_UPDATED = {
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
            "settings": {
              "type": "object",
              "properties": {
                "scheduled_meeting": {
                  "type": "object",
                  "properties": {
                    "host_video": {
                      "type": "string"
                    },
                    "participants_video": {
                      "type": "string"
                    },
                    "audio_type": {
                      "type": "string"
                    },
                    "join_before_host": {
                      "type": "string"
                    },
                    "force_pmi_jbh_password": {
                      "type": "string"
                    },
                    "pstn_password_protected": {
                      "type": "string"
                    }
                  }
                },
                "in_meeting": {
                  "type": "object",
                  "properties": {
                    "e2e_encryption": {
                      "type": "string"
                    },
                    "chat": {
                      "type": "string"
                    },
                    "private_chat": {
                      "type": "string"
                    },
                    "auto_saving_chat": {
                      "type": "string"
                    },
                    "entry_exit_chime": {
                      "type": "string"
                    },
                    "record_play_voice": {
                      "type": "string"
                    },
                    "file_transfer": {
                      "type": "string"
                    },
                    "feedback": {
                      "type": "string"
                    },
                    "co_host": {
                      "type": "string"
                    },
                    "polling": {
                      "type": "string"
                    },
                    "attendee_on_hold": {
                      "type": "string"
                    },
                    "annotation": {
                      "type": "string"
                    },
                    "remote_control": {
                      "type": "string"
                    },
                    "non_verbal_feedback": {
                      "type": "string"
                    },
                    "breakout_room": {
                      "type": "string"
                    },
                    "remote_support": {
                      "type": "string"
                    },
                    "closed_caption": {
                      "type": "string"
                    },
                    "group_hd": {
                      "type": "string"
                    },
                    "virtual_background": {
                      "type": "string"
                    },
                    "far_end_camera_control": {
                      "type": "string"
                    },
                    "share_dual_camera": {
                      "type": "string"
                    },
                    "attention_tracking": {
                      "type": "string"
                    },
                    "waiting_room": {
                      "type": "string"
                    }
                  }
                },
                "email_notification": {
                  "type": "object",
                  "properties": {
                    "jbh_reminder": {
                      "type": "string"
                    },
                    "cancel_meeting_reminder": {
                      "type": "string"
                    },
                    "alternative_host_reminder": {
                      "type": "string"
                    }
                  }
                },
                "recording": {
                  "type": "object",
                  "properties": {
                    "local_recording": {
                      "type": "string"
                    },
                    "cloud_recording": {
                      "type": "string"
                    },
                    "record_speaker_view": {
                      "type": "string"
                    },
                    "record_gallery_view": {
                      "type": "string"
                    },
                    "record_audio_file": {
                      "type": "string"
                    },
                    "save_chat_text": {
                      "type": "string"
                    },
                    "show_timestamp": {
                      "type": "string"
                    },
                    "recording_audio_transcript": {
                      "type": "string"
                    },
                    "auto_recording": {
                      "type": "string"
                    },
                    "auto_delete_cmr": {
                      "type": "string"
                    },
                    "auto_delete_cmr_days": {
                      "type": "string"
                    }
                  }
                },
                "telephony": {
                  "type": "object",
                  "properties": {
                    "third_party_audio": {
                      "type": "string"
                    },
                    "audio_conference_info": {
                      "type": "string"
                    },
                    "show_international_numbers_link": {
                      "type": "string"
                    }
                  }
                },
                "feature": {
                  "type": "object",
                  "properties": {
                    "meeting_capacity": {
                      "type": "string"
                    },
                    "large_meeting": {
                      "type": "string"
                    },
                    "large_meeting_capacity": {
                      "type": "string"
                    },
                    "webinar": {
                      "type": "string"
                    },
                    "webinar_capacity": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        },
        "old_object": {
          "type": "object",
          "properties": {
            "$changed_category": {
              "type": "object",
              "properties": {
                "$changed_field_name": {
                  "type": "string"
                }
              }
            }
          }
        }
      }
    }
  }
}

USER_ACTIVATED = {
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
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "email": {
              "type": "string"
            },
            "type": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}

USER_DEACTIVATED = {
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
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "email": {
              "type": "string"
            },
            "type": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}

USER_DISASSOCIATED = {
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
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "email": {
              "type": "string"
            },
            "type": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}

USER_DELETED = {
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
            "first_name": {
              "type": "string"
            },
            "last_name": {
              "type": "string"
            },
            "email": {
              "type": "string"
            },
            "type": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}