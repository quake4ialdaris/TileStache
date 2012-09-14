'''
Created on Aug 13, 2012

@author: jeff
'''

tags = {
("building", "yes"): 0,
("highway", "residential"): 1,
("highway", "service"): 2,
("waterway", "stream"): 3,
("highway", "unclassified"): 4,
("highway", "track"): 5,
("oneway", "yes"): 6,
("natural", "water"): 7,
("highway", "footway"): 8,
("access", "private"): 9,
("highway", "tertiary"): 10,
("highway", "path"): 11,
("highway", "secondary"): 12,
("landuse", "forest"): 13,
("bridge", "yes"): 14,
("natural", "tree"): 15,
("surface", "paved"): 16,
("natural", "wood"): 17,
("highway", "primary"): 18,
("landuse", "grass"): 19,
("landuse", "residential"): 20,
("surface", "unpaved"): 21,
("highway", "bus_stop"): 22,
("surface", "asphalt"): 23,
("bicycle", "yes"): 24,
("amenity", "parking"): 25,
("place", "locality"): 26,
("railway", "rail"): 27,
("service", "parking_aisle"): 28,
("boundary", "administrative"): 29,
("building", "house"): 30,
("place", "village"): 31,
("natural", "coastline"): 32,
("tracktype", "grade2"): 33,
("oneway", "no"): 34,
("service", "driveway"): 35,
("highway", "turning_circle"): 36,
("place", "hamlet"): 37,
("natural", "wetland"): 38,
("tracktype", "grade3"): 39,
("waterway", "river"): 40,
("highway", "cycleway"): 41,
("barrier", "fence"): 42,
("building", "residential"): 43,
("amenity", "school"): 44,
("highway", "crossing"): 45,
("admin_level", "8"): 46,
("highway", "trunk"): 47,
("amenity", "place_of_worship"): 48,
("landuse", "farmland"): 49,
("tracktype", "grade1"): 50,
("highway", "road"): 51,
("landuse", "farm"): 52,
("surface", "gravel"): 53,
("landuse", "meadow"): 54,
("highway", "motorway"): 55,
("highway", "traffic_signals"): 56,
("building", "hut"): 57,
("highway", "motorway_link"): 58,
("tracktype", "grade4"): 59,
("barrier", "gate"): 60,
("highway", "living_street"): 61,
("bicycle", "no"): 62,
("leisure", "pitch"): 63,
("tunnel", "yes"): 64,
("surface", "ground"): 65,
("highway", "steps"): 66,
("natural", "land"): 67,
("man_made", "survey_point"): 68,
("tracktype", "grade5"): 69,
("waterway", "ditch"): 70,
("leisure", "park"): 71,
("amenity", "restaurant"): 72,
("barrier", "wall"): 73,
("waterway", "riverbank"): 74,
("amenity", "bench"): 75,
("building", "garage"): 76,
("natural", "scrub"): 77,
("highway", "pedestrian"): 78,
("natural", "peak"): 79,
("building", "entrance"): 80,
("landuse", "reservoir"): 81,
("access", "yes"): 82,
("bicycle", "designated"): 83,
("leisure", "swimming_pool"): 84,
("landuse", "farmyard"): 85,
("railway", "level_crossing"): 86,
("building", "apartments"): 87,
("surface", "grass"): 88,
("wheelchair", "yes"): 89,
("service", "alley"): 90,
("landuse", "industrial"): 91,
("amenity", "fuel"): 92,
("surface", "dirt"): 93,
("highway", "trunk_link"): 94,
("waterway", "drain"): 95,
("barrier", "hedge"): 96,
("amenity", "grave_yard"): 97,
("tourism", "information"): 98,
("shop", "supermarket"): 99,
("highway", "primary_link"): 100,
("wood", "deciduous"): 101,
("leisure", "playground"): 102,
("building", "roof"): 103,
("building", "industrial"): 104,
("amenity", "post_box"): 105,
("waterway", "canal"): 106,
("barrier", "bollard"): 107,
("leisure", "garden"): 108,
("wood", "mixed"): 109,
("landuse", "cemetery"): 110,
("landuse", "orchard"): 111,
("shop", "convenience"): 112,
("access", "permissive"): 113,
("surface", "concrete"): 114,
("surface", "paving_stones"): 115,
("service", "spur"): 116,
("building", "garages"): 117,
("amenity", "bank"): 118,
("tourism", "hotel"): 119,
("access", "no"): 120,
("amenity", "fast_food"): 121,
("man_made", "pier"): 122,
("amenity", "kindergarten"): 123,
("access", "agricultural"): 124,
("surface", "cobblestone"): 125,
("wheelchair", "no"): 126,
("amenity", "cafe"): 127,
("amenity", "hospital"): 128,
("amenity", "post_office"): 129,
("amenity", "public_building"): 130,
("amenity", "recycling"): 131,
("highway", "street_lamp"): 132,
("man_made", "tower"): 133,
("waterway", "dam"): 134,
("amenity", "pub"): 135,
("wood", "coniferous"): 136,
("access", "destination"): 137,
("admin_level", "6"): 138,
("landuse", "commercial"): 139,
("amenity", "pharmacy"): 140,
("railway", "abandoned"): 141,
("service", "yard"): 142,
("place", "island"): 143,
("oneway", "-1"): 144,
("landuse", "quarry"): 145,
("landuse", "vineyard"): 146,
("highway", "motorway_junction"): 147,
("railway", "station"): 148,
("landuse", "allotments"): 149,
("barrier", "lift_gate"): 150,
("admin_level", "10"): 151,
("amenity", "telephone"): 152,
("place", "town"): 153,
("man_made", "cutline"): 154,
("place", "suburb"): 155,
("aeroway", "taxiway"): 156,
("wheelchair", "limited"): 157,
("highway", "secondary_link"): 158,
("leisure", "sports_centre"): 159,
("amenity", "bicycle_parking"): 160,
("surface", "sand"): 161,
("highway", "stop"): 162,
("man_made", "works"): 163,
("landuse", "retail"): 164,
("amenity", "fire_station"): 165,
("service", "siding"): 166,
("amenity", "toilets"): 167,
("bench", "yes"): 168,
("oneway", "1"): 169,
("surface", "compacted"): 170,
("landuse", "basin"): 171,
("amenity", "police"): 172,
("railway", "tram"): 173,
("route", "road"): 174,
("natural", "cliff"): 175,
("highway", "construction"): 176,
("aeroway", "aerodrome"): 177,
("entrance", "yes"): 178,
("man_made", "storage_tank"): 179,
("amenity", "atm"): 180,
("tourism", "attraction"): 181,
("route", "bus"): 182,
("shop", "bakery"): 183,
("tourism", "viewpoint"): 184,
("amenity", "swimming_pool"): 185,
("natural", "beach"): 186,
("tourism", "picnic_site"): 187,
("oneway", "true"): 188,
("highway", "bridleway"): 189,
("tourism", "camp_site"): 190,
("abutters", "residential"): 191,
("leisure", "nature_reserve"): 192,
("amenity", "drinking_water"): 193,
("shop", "clothes"): 194,
("natural", "heath"): 195,
("highway", "mini_roundabout"): 196,
("landuse", "construction"): 197,
("amenity", "waste_basket"): 198,
("railway", "platform"): 199,
("amenity", "townhall"): 200,
("shop", "hairdresser"): 201,
("amenity", "shelter"): 202,
("admin_level", "9"): 203,
("building", "farm_auxiliary"): 204,
("amenity", "library"): 205,
("building", "detached"): 206,
("admin_level", "4"): 207,
("landuse", "village_green"): 208,
("barrier", "stile"): 209,
("landuse", "garages"): 210,
("amenity", "bar"): 211,
("railway", "buffer_stop"): 212,
("wetland", "marsh"): 213,
("tourism", "museum"): 214,
("barrier", "cycle_barrier"): 215,
("route", "bicycle"): 216,
("railway", "tram_stop"): 217,
("amenity", "parking_space"): 218,
("barrier", "retaining_wall"): 219,
("landuse", "recreation_ground"): 220,
("amenity", "university"): 221,
("highway", "tertiary_link"): 222,
("building", "terrace"): 223,
("shop", "car_repair"): 224,
("amenity", "hunting_stand"): 225,
("amenity", "fountain"): 226,
("man_made", "pipeline"): 227,
("wetland", "swamp"): 228,
("shop", "car"): 229,
("bench", "no"): 230,
("tunnel", "culvert"): 231,
("building", "school"): 232,
("barrier", "entrance"): 233,
("railway", "disused"): 234,
("railway", "crossing"): 235,
("building", "church"): 236,
("amenity", "social_facility"): 237,
("natural", "bay"): 238,
("shop", "kiosk"): 239,
("amenity", "vending_machine"): 240,
("route", "hiking"): 241,
("natural", "spring"): 242,
("leisure", "common"): 243,
("railway", "switch"): 244,
("waterway", "rapids"): 245,
("admin_level", "7"): 246,
("leisure", "stadium"): 247,
("leisure", "track"): 248,
("place", "isolated_dwelling"): 249,
("place", "islet"): 250,
("waterway", "weir"): 251,
("amenity", "doctors"): 252,
("access", "designated"): 253,
("landuse", "conservation"): 254,
("waterway", "artificial"): 255,
("amenity", "bus_station"): 256,
("leisure", "golf_course"): 257,
("shop", "doityourself"): 258,
("building", "service"): 259,
("tourism", "guest_house"): 260,
("aeroway", "runway"): 261,
("place", "city"): 262,
("railway", "subway"): 263,
("man_made", "wastewater_plant"): 264,
("building", "commercial"): 265,
("railway", "halt"): 266,
("amenity", "emergency_phone"): 267,
("building", "retail"): 268,
("barrier", "block"): 269,
("leisure", "recreation_ground"): 270,
("access", "forestry"): 271,
("amenity", "college"): 272,
("highway", "platform"): 273,
("access", "unknown"): 274,
("man_made", "water_tower"): 275,
("surface", "pebblestone"): 276,
("bridge", "viaduct"): 277,
("shop", "butcher"): 278,
("shop", "florist"): 279,
("boundary", "landuse"): 280,
("aeroway", "helipad"): 281,
("building", "hangar"): 282,
("natural", "glacier"): 283,
("highway", "proposed"): 284,
("shop", "mall"): 285,
("barrier", "toll_booth"): 286,
("amenity", "fire_hydrant"): 287,
("building", "manufacture"): 288,
("building", "farm"): 289,
("surface", "wood"): 290,
("amenity", "car_wash"): 291,
("amenity", "dentist"): 292,
("natural", "marsh"): 293,
("man_made", "surveillance"): 294,
("shop", "bicycle"): 295,
("route", "foot"): 296,
("amenity", "theatre"): 297,
("building", "office"): 298,
("railway", "light_rail"): 299,
("man_made", "petroleum_well"): 300,
("amenity", "taxi"): 301,
("building", "greenhouse"): 302,
("landuse", "brownfield"): 303,
("bicycle", "permissive"): 304,
("admin_level", "2"): 305,
("aeroway", "apron"): 306,
("building", "cabin"): 307,
("amenity", "cinema"): 308,
("access", "customers"): 309,
("tourism", "motel"): 310,
("railway", "narrow_gauge"): 311,
("amenity", "marketplace"): 312,
("shop", "furniture"): 313,
("entrance", "staircase"): 314,
("tourism", "artwork"): 315,
("natural", "grassland"): 316,
("shop", "books"): 317,
("admin_level", "5"): 318,
("man_made", "groyne"): 319,
("waterway", "lock_gate"): 320,
("highway", "emergency_access_point"): 321,
("natural", "sand"): 322,
("landuse", "military"): 323,
("boundary", "protected_area"): 324,
("amenity", "community_centre"): 325,
("barrier", "kissing_gate"): 326,
("highway", "speed_camera"): 327,
("boundary", "national_park"): 328,
("railway", "subway_entrance"): 329,
("man_made", "silo"): 330,
("shop", "alcohol"): 331,
("highway", "give_way"): 332,
("leisure", "slipway"): 333,
("shop", "electronics"): 334,
("bicycle", "dismount"): 335,
("leisure", "marina"): 336,
("entrance", "main"): 337,
("boundary", "postal_code"): 338,
("landuse", "greenhouse_horticulture"): 339,
("highway", "milestone"): 340,
("natural", "cave_entrance"): 341,
("landuse", "landfill"): 342,
("shop", "chemist"): 343,
("shop", "shoes"): 344,
("barrier", "cattle_grid"): 345,
("landuse", "railway"): 346,
("tourism", "hostel"): 347,
("tourism", "chalet"): 348,
("place", "county"): 349,
("shop", "department_store"): 350,
("highway", "ford"): 351,
("natural", "scree"): 352,
("landuse", "greenfield"): 353,
("amenity", "nursing_home"): 354,
("barrier", "wire_fence"): 355,
("access", "restricted"): 356,
("man_made", "reservoir_covered"): 357,
("amenity", "bicycle_rental"): 358,
("man_made", "MDF"): 359,
("man_made", "water_well"): 360,
("landuse", "field"): 361,
("landuse", "wood"): 362,
("shop", "hardware"): 363,
("tourism", "alpine_hut"): 364,
("natural", "tree_row"): 365,
("tourism", "caravan_site"): 366,
("bridge", "no"): 367,
("wetland", "bog"): 368,
("amenity", "courthouse"): 369,
("route", "ferry"): 370,
("barrier", "city_wall"): 371,
("amenity", "veterinary"): 372,
("shop", "jewelry"): 373,
("building", "transportation"): 374,
("amenity", "arts_centre"): 375,
("bicycle", "official"): 376,
("shop", "optician"): 377,
("shop", "yes"): 378,
("building", "collapsed"): 379,
("shop", "garden_centre"): 380,
("man_made", "chimney"): 381,
("man_made", "mine"): 382,
("bench", "unknown"): 383,
("railway", "preserved"): 384,
("building", "public"): 385,
("amenity", "ferry_terminal"): 386,
("highway", "raceway"): 387,
("natural", "rock"): 388,
("tunnel", "no"): 389,
("building", "university"): 390,
("shop", "beverages"): 391,
("amenity", "waste_disposal"): 392,
("building", "warehouse"): 393,
("leisure", "water_park"): 394,
("shop", "gift"): 395,
("place", "farm"): 396,
("wetland", "tidalflat"): 397,
("waterway", "waterfall"): 398,
("man_made", "dolphin"): 399,
("service", "drive-through"): 400,
("amenity", "nightclub"): 401,
("building", "shed"): 402,
("shop", "greengrocer"): 403,
("natural", "fell"): 404,
("wetland", "wet_meadow"): 405,
("aeroway", "gate"): 406,
("shop", "computer"): 407,
("man_made", "lighthouse"): 408,
("wetland", "reedbed"): 409,
("man_made", "breakwater"): 410,
("surface", "Dirt/Sand"): 411,
("barrier", "ditch"): 412,
("barrier", "yes"): 413,
("amenity", "biergarten"): 414,
("shop", "mobile_phone"): 415,
("route", "mtb"): 416,
("amenity", "grit_bin"): 417,
("amenity", "bbq"): 418,
("shop", "sports"): 419,
("barrier", "wood_fence"): 420,
("entrance", "home"): 421,
("shop", "laundry"): 422,
("man_made", "gasometer"): 423,
("barrier", "embankment"): 424,
("shop", "toys"): 425,
("wetland", "saltmarsh"): 426,
("waterway", "soakhole"): 427,
("shop", "travel_agency"): 428,
("man_made", "water_works"): 429,
("route", "railway"): 430,
("amenity", "prison"): 431,
("highway", "rest_area"): 432,
("shop", "stationery"): 433,
("admin_level", "11"): 434,
("building", "train_station"): 435,
("building", "storage_tank"): 436,
("man_made", "windmill"): 437,
("shop", "beauty"): 438,
("building", "semi"): 439,
("highway", "services"): 440,
("bicycle", "private"): 441,
("route", "ski"): 442,
("service", "emergency_access"): 443,
("building", "factory"): 444,
("man_made", "reinforced_slope"): 445,
("amenity", "car_sharing"): 446,
("surface", "earth"): 447,
("shop", "hifi"): 448,
("amenity", "car_rental"): 449,
("barrier", "hedge_bank"): 450,
("shop", "confectionery"): 451,
("aeroway", "terminal"): 452,
("highway", "passing_place"): 453,
("building", "building"): 454,
("man_made", "dyke"): 455,
("building", "construction"): 456,
("building", "shop"): 457,
("natural", "reef"): 458,
("landuse", "aquaculture"): 459,
("shop", "dry_cleaning"): 460,
("amenity", "embassy"): 461,
("shop", "newsagent"): 462,
("landuse", "salt_pond"): 463,
("railway", "spur"): 464,
("wheelchair", "unknown"): 465,
("tourism", "zoo"): 466,
("man_made", "waterway"): 467,
("surface", "fine_gravel"): 468,
("shop", "motorcycle"): 469,
("building", "Building"): 470,
("railway", "construction"): 471,
("place", "neighbourhood"): 472,
("route", "train"): 473,
("building", "no"): 474,
("natural", "mud"): 475,
("place", "region"): 476,
("landuse", "reservoir_watershed"): 477,
("boundary", "marker"): 478,
("man_made", "beacon"): 479,
("shop", "outdoor"): 480,
("access", "public"): 481,
("abutters", "industrial"): 482,
("building", "barn"): 483,
("leisure", "picnic_table"): 484,
("building", "hospital"): 485,
("access", "official"): 486,
("shop", "variety_store"): 487,
("man_made", "crane"): 488,
("amenity", "parking;fuel"): 489,
("route", "tram"): 490,
("tourism", "theme_park"): 491,
("shop", "pet"): 492,
("building", "kindergarten"): 493,
("man_made", "storage"): 494,
("man_made", "mast"): 495,
("amenity", "parking_entrance"): 496,
("amenity", "clock"): 497,
("landuse", "industrial;retail"): 498,
("shop", "video"): 499,
("access", "delivery"): 500,
("amenity", "driving_school"): 501,
("service", "yes"): 502,
("natural", "bare_rock"): 503,
("building", "chapel"): 504,
("natural", "volcano"): 505,
("waterway", "dock"): 506,
("building", "dormitory"): 507,
("amenity", "boat_storage"): 508,
("man_made", "tank"): 509,
("man_made", "flagpole"): 510,
("surface", "grass_paver"): 511,
("shop", "organic"): 512,
("natural", "landform"): 513,
("highway", "unsurfaced"): 514,
("route", "power"): 515,
("surface", "mud"): 516,
("building", "building_concrete"): 517,
("abutters", "retail"): 518,
("building", "store"): 519,
("shop", "vacant"): 520,
("leisure", "miniature_golf"): 521,
("man_made", "monitoring_station"): 522,
("natural", "waterfall"): 523,
("aeroway", "hangar"): 524,
("shop", "boutique"): 525,
("route", "detour"): 526,
("building", "way"): 527,
("railway", "stop"): 528,
("amenity", "ice_cream"): 529,
("building", "storage"): 530,
("shop", "car_parts"): 531,
("natural", "ridge"): 532,
("shop", "tyres"): 533,
("railway", "dismantled"): 534,
("amenity", "shop"): 535,
("landuse", "plant_nursery"): 536,
("building", "residentiel1"): 537,
("barrier", "field_boundary"): 538,
("barrier", "border_control"): 539,
("surface", "Paved"): 540,
("barrier", "sally_port"): 541,
("amenity", "bureau_de_change"): 542,
("leisure", "fishing"): 543,
("amenity", "charging_station"): 544,
("building", "supermarket"): 545,
("highway", "stile"): 546,
("amenity", "sauna"): 547,
("place", "municipality"): 548,
("building", "hotel"): 549,
("surface", "metal"): 550,
("highway", "incline_steep"): 551,
("shop", "estate_agent"): 552,
("natural", "grass"): 553,
("shop", "pharmacy"): 554,
("surface", "concrete:plates"): 555,
("shop", "copyshop"): 556,
("surface", "paving_stones:30"): 557,
("surface", "interlock"): 558,
("access", "hov"): 559,
("highway", "elevator"): 560,
("boundary", "local_authority"): 561,
("man_made", "communications_tower"): 562,
("shop", "deli"): 563,
("barrier", "turnstile"): 564,
("building", "offices"): 565,
("building", "bunker"): 566,
("natural", "stone"): 567,
("railway", "railway_crossing"): 568,
("leisure", "dog_park"): 569,
("building", "semi-detached"): 570,
("man_made", "watermill"): 571,
("route", "trolleybus"): 572,
("admin_level", "3"): 573,
("building", "block"): 574,
("barrier", "guard_rail"): 575,
("bicycle", "unknown"): 576,
("highway", "abandoned"): 577,
("surface", "dirt/sand"): 578,
("barrier", "chain"): 579,
("barrier", "bump_gate"): 580,
("building", "residental"): 581,
("surface", "cement"): 582,
("man_made", "embankment"): 583,
("building", "ruins"): 584,
("highway", "incline"): 585,
("abutters", "commercial"): 586,
("barrier", "hampshire_gate"): 587,
("shop", "music"): 588,
("shop", "funeral_directors"): 589,
("wetland", "mangrove"): 590,
("place", "borough"): 591,
("building", "apartment"): 592,
("boundary", "census"): 593,
("barrier", "kerb"): 594,
("building", "glasshouse"): 595,
("aeroway", "holding_position"): 596,
("shop", "general"): 597,
("building", "tank"): 598,
("railway", "monorail"): 599,
("service", "parking"): 600,
("place", "state"): 601,
("railway", "proposed"): 602,
("shop", "art"): 603,
("natural", "hill"): 604,
("railway", "turntable"): 605,
("tourism", "cabin"): 606,
("shop", "photo"): 607,
("boundary", "lot"): 608,
("shop", "fishmonger"): 609,
("amenity", "clinic"): 610,
("boundary", "political"): 611,
("man_made", "well"): 612,
("highway", "byway"): 613,
("leisure", "horse_riding"): 614,
("service", "bus"): 615,
("building", "tower"): 616,
("entrance", "service"): 617,
("shop", "fabric"): 618,
("railway", "miniature"): 619,
("abutters", "mixed"): 620,
("surface", "stone"): 621,
("access", "emergency"): 622,
("landuse", "mine"): 623,
("amenity", "shower"): 624,
("waterway", "lock"): 625,
("area", "yes"): 626
}

    

def getTags():
        return tags
