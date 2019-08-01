RECORDING_REGISTARTION_APPROVED = {
  "type": "object",
  "properties": {
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
            "registrant": {
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
                }
              }
            }
          }
        }
      }
    },
    "event": {
      "type": "string"
    }
  }
}

RECORDING_REGISTRATION_DENIED = {
  "type": "object",
  "properties": {
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
            "registrant": {
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
                }
              }
            }
          }
        }
      }
    },
    "event": {
      "type": "string"
    }
  }
}

RECORDING_REGISTRATION = {
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
                }
              }
            }
          }
        }
      }
    }
  }
}

RECORDING_RECOVERED = {
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
            "share_url": {
              "type": "string"
            },
            "total_size": {
              "type": "string"
            },
            "recording_count": {
              "type": "string"
            },
            "recording_files": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "meeting_id": {
                    "type": "string"
                  },
                  "recording_start": {
                    "type": "string"
                  },
                  "recording_end": {
                    "type": "string"
                  },
                  "file_type": {
                    "type": "string"
                  },
                  "file_size": {
                    "type": "string"
                  },
                  "play_url": {
                    "type": "string"
                  },
                  "download_url": {
                    "type": "string"
                  },
                  "status": {
                    "type": "string"
                  },
                  "recording_type": {
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

RECORDING_DELETED = {
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
            "share_url": {
              "type": "string"
            },
            "total_size": {
              "type": "string"
            },
            "recording_count": {
              "type": "string"
            },
            "recording_files": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "meeting_id": {
                    "type": "string"
                  },
                  "recording_start": {
                    "type": "string"
                  },
                  "recording_end": {
                    "type": "string"
                  },
                  "file_type": {
                    "type": "string"
                  },
                  "file_size": {
                    "type": "string"
                  },
                  "play_url": {
                    "type": "string"
                  },
                  "download_url": {
                    "type": "string"
                  },
                  "status": {
                    "type": "string"
                  },
                  "recording_type": {
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

RECORDING_RESUMED = {
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
            "recording_file": {
              "type": "object",
              "properties": {
                "recording_start": {
                  "type": "string"
                },
                "recording_end": {
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

RECORDING_THRASHED = {
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
            "share_url": {
              "type": "string"
            },
            "total_size": {
              "type": "string"
            },
            "recording_count": {
              "type": "string"
            },
            "recording_files": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "meeting_id": {
                    "type": "string"
                  },
                  "recording_start": {
                    "type": "string"
                  },
                  "recording_end": {
                    "type": "string"
                  },
                  "file_type": {
                    "type": "string"
                  },
                  "file_size": {
                    "type": "string"
                  },
                  "play_url": {
                    "type": "string"
                  },
                  "download_url": {
                    "type": "string"
                  },
                  "status": {
                    "type": "string"
                  },
                  "recording_type": {
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

RECORDING_STARTED = {
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
            "recording_file": {
              "type": "object",
              "properties": {
                "recording_start": {
                  "type": "string"
                },
                "recording_end": {
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

RECORDING_STOPPED = {
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
            "recording_file": {
              "type": "object",
              "properties": {
                "recording_start": {
                  "type": "string"
                },
                "recording_end": {
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

RECORDING_PAUSED = {
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
            "recording_file": {
              "type": "object",
              "properties": {
                "recording_start": {
                  "type": "string"
                },
                "recording_end": {
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

RECORDING_REGISTRATION_CREATED = {
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
                }
              }
            }
          }
        }
      }
    }
  }
}

RECORDING_TRANSCRIPT_COMPLETED = {
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
            "share_url": {
              "type": "string"
            },
            "total_size": {
              "type": "string"
            },
            "recording_count": {
              "type": "string"
            },
            "recording_files": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "meeting_id": {
                    "type": "string"
                  },
                  "recording_start": {
                    "type": "string"
                  },
                  "recording_end": {
                    "type": "string"
                  },
                  "file_type": {
                    "type": "string"
                  },
                  "file_size": {
                    "type": "string"
                  },
                  "play_url": {
                    "type": "string"
                  },
                  "download_url": {
                    "type": "string"
                  },
                  "status": {
                    "type": "string"
                  },
                  "recording_type": {
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

RECORDING_COMPLETED = {
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
            "share_url": {
              "type": "string"
            },
            "total_size": {
              "type": "string"
            },
            "recording_count": {
              "type": "string"
            },
            "recording_files": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "meeting_id": {
                    "type": "string"
                  },
                  "recording_start": {
                    "type": "string"
                  },
                  "recording_end": {
                    "type": "string"
                  },
                  "file_type": {
                    "type": "string"
                  },
                  "file_size": {
                    "type": "string"
                  },
                  "play_url": {
                    "type": "string"
                  },
                  "download_url": {
                    "type": "string"
                  },
                  "status": {
                    "type": "string"
                  },
                  "recording_type": {
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