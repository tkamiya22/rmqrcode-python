from enums.error_collection_level import ErrorCollectionLevel

qr_versions = {
    'R7x43': {
        'version_indicator': 0b00000,
        'height': 7,
        'width': 43,
        'reminder_bits': 0,
        'character_count_length': 3,
        'codewords_total': 13,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 13,
                    'k': 6,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 13,
                    'k': 3,
                },
            ]
        }
    },
    'R7x59': {
        'version_indicator': 0b00001,
        'height': 7,
        'width': 59,
        'reminder_bits': 3,
        'character_count_length': 4,
        'codewords_total': 21,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 21,
                    'k': 12,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 21,
                    'k': 7,
                },
            ]
        }
    },
    'R7x77': {
        'version_indicator': 0b00010,
        'height': 7,
        'width': 77,
        'reminder_bits': 5,
        'character_count_length': 5,
        'codewords_total': 32,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 32,
                    'k': 20,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 32,
                    'k': 10,
                },
            ]
        }
    },
    'R7x99': {
        'version_indicator': 0b00011,
        'height': 7,
        'width': 99,
        'reminder_bits': 6,
        'character_count_length': 5,
        'codewords_total': 44,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 44,
                    'k': 28,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 44,
                    'k': 14,
                },
            ]
        }
    },
    'R7x139': {
        'version_indicator': 0b00100,
        'height': 7,
        'width': 139,
        'reminder_bits': 1,
        'character_count_length': 6,
        'codewords_total': 68,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 68,
                    'k': 44,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 2,
                    'c': 34,
                    'k': 12,
                },
            ]
        }
    },
    'R9x43': {
        'version_indicator': 0b00101,
        'height': 9,
        'width': 43,
        'reminder_bits': 2,
        'character_count_length': 4,
        'codewords_total': 21,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 21,
                    'k': 12,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 21,
                    'k': 7,
                },
            ]
        }
    },
    'R9x59': {
        'version_indicator': 0b00110,
        'height': 9,
        'width': 59,
        'reminder_bits': 3,
        'character_count_length': 5,
        'codewords_total': 33,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 33,
                    'k': 21,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 33,
                    'k': 11,
                },
            ]
        }
    },
    'R9x77': {
        'version_indicator': 0b00111,
        'height': 9,
        'width': 77,
        'reminder_bits': 1,
        'character_count_length': 5,
        'codewords_total': 49,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 49,
                    'k': 31,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 24,
                    'k': 8,
                },
                {
                    'num': 1,
                    'c': 25,
                    'k': 9,
                },
            ]
        }
    },
    'R9x99': {
        'version_indicator': 0b01000,
        'height': 9,
        'width': 99,
        'reminder_bits': 4,
        'character_count_length': 6,
        'codewords_total': 66,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 66,
                    'k': 42,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 2,
                    'c': 33,
                    'k': 11,
                },
            ]
        }
    },
    'R9x139': {
        'version_indicator': 0b01001,
        'height': 9,
        'width': 139,
        'reminder_bits': 5,
        'character_count_length': 6,
        'codewords_total': 99,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 49,
                    'k': 31,
                },
                {
                    'num': 1,
                    'c': 50,
                    'k': 32,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 3,
                    'c': 33,
                    'k': 11,
                }
            ]
        }
    },
    'R11x27': {
        'version_indicator': 0b01010,
        'height': 11,
        'width': 27,
        'reminder_bits': 2,
        'character_count_length': 3,
        'codewords_total': 15,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 15,
                    'k': 7,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 15,
                    'k': 5,
                }
            ]
        }
    },
    'R11x43': {
        'version_indicator': 0b01011,
        'height': 11,
        'width': 43,
        'reminder_bits': 1,
        'character_count_length': 5,
        'codewords_total': 31,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 31,
                    'k': 19,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 31,
                    'k': 11,
                }
            ]
        }
    },
    'R11x59': {
        'version_indicator': 0b01100,
        'height': 11,
        'width': 59,
        'reminder_bits': 0,
        'character_count_length': 5,
        'codewords_total': 47,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 47,
                    'k': 31,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 23,
                    'k': 7,
                },
                {
                    'num': 1,
                    'c': 24,
                    'k': 8,
                },
            ]
        }
    },
    'R11x77': {
        'version_indicator': 0b01101,
        'height': 11,
        'width': 77,
        'reminder_bits': 2,
        'character_count_length': 6,
        'codewords_total': 67,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 67,
                    'k': 43,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 33,
                    'k': 11,
                },
                {
                    'num': 1,
                    'c': 34,
                    'k': 12,
                },
            ]
        }
    },
    'R11x99': {
        'version_indicator': 0b01110,
        'height': 11,
        'width': 99,
        'reminder_bits': 7,
        'character_count_length': 6,
        'codewords_total': 89,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 44,
                    'k': 28,
                },
                {
                    'num': 1,
                    'c': 45,
                    'k': 29,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 44,
                    'k': 14,
                },
                {
                    'num': 1,
                    'c': 45,
                    'k': 15,
                },
            ]
        }
    },
    'R11x139': {
        'version_indicator': 0b01111,
        'height': 11,
        'width': 139,
        'reminder_bits': 6,
        'character_count_length': 7,
        'codewords_total': 132,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 2,
                    'c': 66,
                    'k': 42,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 3,
                    'c': 44,
                    'k': 14,
                }
            ]
        }
    },
    'R13x27': {
        'version_indicator': 0b10000,
        'height': 13,
        'width': 27,
        'character_count_length': 4,
        'reminder_bits': 4,
        'codewords_total': 21,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 21,
                    'k': 14,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 21,
                    'k': 7,
                }
            ]
        }
    },
    'R13x43': {
        'version_indicator': 0b10001,
        'height': 13,
        'width': 43,
        'reminder_bits': 1,
        'character_count_length': 5,
        'codewords_total': 41,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 41,
                    'k': 27,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 41,
                    'k': 13,
                }
            ]
        }
    },
    'R13x59': {
        'version_indicator': 0b10010,
        'height': 13,
        'width': 59,
        'reminder_bits': 6,
        'character_count_length': 6,
        'codewords_total': 60,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 60,
                    'k': 38,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 2,
                    'c': 30,
                    'k': 10,
                }
            ]
        }
    },
    'R13x77': {
        'version_indicator': 0b10011,
        'height': 13,
        'width': 77,
        'reminder_bits': 4,
        'character_count_length': 6,
        'codewords_total': 85,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 42,
                    'k': 26,
                },
                {
                    'num': 1,
                    'c': 43,
                    'k': 27,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 42,
                    'k': 14,
                },
                {
                    'num': 1,
                    'c': 43,
                    'k': 15,
                },
            ]
        }
    },
    'R13x99': {
        'version_indicator': 0b10100,
        'height': 13,
        'width': 99,
        'reminder_bits': 3,
        'character_count_length': 7,
        'codewords_total': 113,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 56,
                    'k': 36,
                },
                {
                    'num': 1,
                    'c': 57,
                    'k': 37,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 37,
                    'k': 11,
                },
                {
                    'num': 2,
                    'c': 38,
                    'k': 12,
                },
            ]
        }
    },
    'R13x139': {
        'version_indicator': 0b10101,
        'height': 13,
        'width': 139,
        'reminder_bits': 0,
        'character_count_length': 7,
        'codewords_total': 166,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 2,
                    'c': 55,
                    'k': 35,
                },
                {
                    'num': 1,
                    'c': 56,
                    'k': 36,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 2,
                    'c': 41,
                    'k': 13,
                },
                {
                    'num': 2,
                    'c': 42,
                    'k': 14,
                },
            ]
        }
    },
    'R15x43': {
        'version_indicator': 0b10110,
        'height': 15,
        'width': 43,
        'reminder_bits': 1,
        'character_count_length': 6,
        'codewords_total': 51,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 51,
                    'k': 33,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 25,
                    'k': 7,
                },
                {
                    'num': 1,
                    'c': 26,
                    'k': 8,
                },
            ]
        }
    },
    'R15x59': {
        'version_indicator': 0b10111,
        'height': 15,
        'width': 59,
        'reminder_bits': 4,
        'character_count_length': 6,
        'codewords_total': 74,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 74,
                    'k': 48,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 2,
                    'c': 37,
                    'k': 13,
                }
            ]
        }
    },
    'R15x77': {
        'version_indicator': 0b11000,
        'height': 15,
        'width': 77,
        'reminder_bits': 6,
        'character_count_length': 7,
        'codewords_total': 103,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 51,
                    'k': 33,
                },
                {
                    'num': 1,
                    'c': 52,
                    'k': 34,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 2,
                    'c': 34,
                    'k': 10,
                },
                {
                    'num': 1,
                    'c': 35,
                    'k': 11,
                },
            ]
        }
    },
    'R15x99': {
        'version_indicator': 0b11001,
        'height': 15,
        'width': 99,
        'reminder_bits': 7,
        'character_count_length': 7,
        'codewords_total': 136,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 2,
                    'c': 68,
                    'k': 44,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 4,
                    'c': 34,
                    'k': 12,
                },
            ],
        }
    },
    'R15x139': {
        'version_indicator': 0b11010,
        'height': 15,
        'width': 139,
        'reminder_bits': 2,
        'character_count_length': 7,
        'codewords_total': 199,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 2,
                    'c': 66,
                    'k': 42,
                },
                {
                    'num': 1,
                    'c': 67,
                    'k': 43,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 39,
                    'k': 13,
                },
                {
                    'num': 4,
                    'c': 40,
                    'k': 14,
                },
            ],
        }
    },
    'R17x43': {
        'version_indicator': 0b11011,
        'height': 17,
        'width': 43,
        'reminder_bits': 1,
        'character_count_length': 6,
        'codewords_total': 61,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 1,
                    'c': 60,
                    'k': 39,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 30,
                    'k': 10,
                },
                {
                    'num': 1,
                    'c': 31,
                    'k': 11,
                },
            ]
        }
    },
    'R17x59': {
        'version_indicator': 0b11100,
        'height': 17,
        'width': 59,
        'reminder_bits': 2,
        'character_count_length': 6,
        'codewords_total': 88,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 2,
                    'c': 44,
                    'k': 28,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 2,
                    'c': 44,
                    'k': 14,
                }
            ]
        }
    },
    'R17x77': {
        'version_indicator': 0b11101,
        'height': 17,
        'width': 77,
        'reminder_bits': 0,
        'character_count_length': 7,
        'codewords_total': 122,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 2,
                    'c': 61,
                    'k': 39,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 1,
                    'c': 40,
                    'k': 12,
                },
                {
                    'num': 2,
                    'c': 41,
                    'k': 13,
                },
            ],
        }
    },
    'R17x99': {
        'version_indicator': 0b11110,
        'height': 17,
        'width': 99,
        'reminder_bits': 3,
        'character_count_length': 7,
        'codewords_total': 160,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 2,
                    'c': 53,
                    'k': 33,
                },
                {
                    'num': 1,
                    'c': 54,
                    'k': 34,
                }
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 4,
                    'c': 40,
                    'k': 14,
                },
            ],
        }
    },
    'R17x139': {
        'version_indicator': 0b11111,
        'height': 17,
        'width': 139,
        'reminder_bits': 4,
        'character_count_length': 8,
        'codewords_total': 232,
        'blocks': {
            ErrorCollectionLevel.M: [
                {
                    'num': 4,
                    'c': 58,
                    'k': 38,
                },
            ],
            ErrorCollectionLevel.H: [
                {
                    'num': 2,
                    'c': 38,
                    'k': 12,
                },
                {
                    'num': 4,
                    'c': 39,
                    'k': 13,
                },
            ],
        }
    },
}
