WEBINAR_STARTED = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "start_time": {
              "type": "string",
              "format": "date-time"
            }
          }
        }
      }
    }
  }
}

WEBINAR_ENDED = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}

WEBINAR_PARTICIPANT_JOINED = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "participant": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "user_id": {
                  "type": "string"
                },
                "user_name": {
                  "type": "string"
                },
                "join_time": {
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

WEBINAR_PARTICIPANT_LEFT = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "participant": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "user_id": {
                  "type": "string"
                },
                "user_name": {
                  "type": "string"
                },
                "join_time": {
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

WEBINAR_CREATED = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "occurrences": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "occurrence_id": {
                    "type": "string"
                  },
                  "start_time": {
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
}

WEBINAR_DELETED = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "occurrences": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "occurrence_id": {
                    "type": "string"
                  },
                  "start_time": {
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
}

WEBINAR_SHARING_ENDED = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "participant": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "user_id": {
                  "type": "string"
                },
                "user_name": {
                  "type": "string"
                },
                "sharing_details": {
                  "type": "object",
                  "properties": {
                    "content": {
                      "type": "string"
                    },
                    "source": {
                      "type": "string"
                    },
                    "file_link": {
                      "type": "string"
                    },
                    "date_time": {
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
  }
}

WEBINAR_SHARING_STARTED = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "participant": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "user_id": {
                  "type": "string"
                },
                "user_name": {
                  "type": "string"
                },
                "sharing_details": {
                  "type": "object",
                  "properties": {
                    "content": {
                      "type": "string"
                    },
                    "source": {
                      "type": "string"
                    },
                    "file_link": {
                      "type": "string"
                    },
                    "date_time": {
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
  }
}

WEBINAR_ALERT = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "issues": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}

WEBINAR_UPDATED = {
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
        "operator_id": {
          "type": "string"
        },
        "object": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string"
            },
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "password": {
              "type": "string"
            },
            "agenda": {
              "type": "string"
            },
            "registration_url": {
              "type": "string"
            },
            "join_url": {
              "type": "string"
            },
            "occurrences": {
              "type": "object",
              "properties": {
                "occurrence_id": {
                  "type": "string"
                },
                "start_time": {
                  "type": "string"
                }
              }
            },
            "recurrence": {
              "type": "object",
              "properties": {
                "type": {
                  "type": "string"
                },
                "repeat_interval": {
                  "type": "string"
                },
                "weekly_days": {
                  "type": "string"
                },
                "monthly_day": {
                  "type": "string"
                },
                "monthly_week": {
                  "type": "string"
                },
                "monthly_week_day": {
                  "type": "string"
                },
                "end_times": {
                  "type": "string"
                },
                "end_date_time": {
                  "type": "string"
                }
              }
            },
            "settings": {
              "type": "object",
              "properties": {
                "host_video": {
                  "type": "string"
                },
                "panelists_video": {
                  "type": "string"
                },
                "practice_session": {
                  "type": "string"
                },
                "approval_type": {
                  "type": "string"
                },
                "registration_type": {
                  "type": "string"
                },
                "audio": {
                  "type": "string"
                },
                "auto_recording": {
                  "type": "string"
                },
                "enforce_login": {
                  "type": "string"
                },
                "enforce_login_domains": {
                  "type": "string"
                },
                "alternative_hosts": {
                  "type": "string"
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
                  "type": [
                    "string",
                    "number",
                    "integer",
                    "boolean",
                    "array"
                  ]
                }
              }
            }
          }
        }
      }
    }
  }
}

WEBINAR_REGISTRATION_APPROVED = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "occurrences": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "occurrence_id": {
                    "type": "string"
                  },
                  "start_time": {
                    "type": "string"
                  }
                }
              }
            },
            "registrant": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "first_name": {
                  "type": "string"
                },
                "last_name": {
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

WEBBINAR_REGISTRATION_CANCELLED = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "occurrences": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "occurrence_id": {
                    "type": "string"
                  },
                  "start_time": {
                    "type": "string"
                  }
                }
              }
            },
            "registrant": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "first_name": {
                  "type": "string"
                },
                "last_name": {
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

WEBINAR_REGISTRATION_DENIED = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "occurrences": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "occurrence_id": {
                    "type": "string"
                  },
                  "start_time": {
                    "type": "string"
                  }
                }
              }
            },
            "registrant": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "first_name": {
                  "type": "string"
                },
                "last_name": {
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

WEBINAR_REGISTRATION_CREATED = {
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
            "uuid": {
              "type": "string"
            },
            "host_id": {
              "type": "string"
            },
            "topic": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "start_time": {
              "type": "string"
            },
            "timezone": {
              "type": "string"
            },
            "duration": {
              "type": "string"
            },
            "occurrences": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "occurrence_id": {
                    "type": "string"
                  },
                  "start_time": {
                    "type": "string"
                  }
                }
              }
            },
            "registrant": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "first_name": {
                  "type": "string"
                },
                "last_name": {
                  "type": "string"
                },
                "address": {
                  "type": "string"
                },
                "city": {
                  "type": "string"
                },
                "country": {
                  "type": "string"
                },
                "zip": {
                  "type": "string"
                },
                "state": {
                  "type": "string"
                },
                "phone": {
                  "type": "string"
                },
                "industry": {
                  "type": "string"
                },
                "org": {
                  "type": "string"
                },
                "job_title": {
                  "type": "string"
                },
                "purchasing_time_frame": {
                  "type": "string"
                },
                "role_in_purchase_process": {
                  "type": "string"
                },
                "no_of_employees": {
                  "type": "string"
                },
                "comments": {
                  "type": "string"
                },
                "custom_questions": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "title": {
                        "type": "string"
                      },
                      "value": {
                        "type": "string"
                      }
                    }
                  }
                },
                "join_url": {
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