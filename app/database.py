# Simulating a database with an in-memory dictionary
dog_db = {
    "Bulldog": {
        "name": "Bulldog",
        "height": 40,
        "weight": 24,
        "breed": "Pure",
        "purpose": "Companion",
        "speciality": "Calm demeanor",
        "origin": "England"
    },
    "German Shepherd": {
        "name": "German Shepherd",
        "height": 65,
        "weight": 30,
        "breed": "Pure",
        "purpose": "Working",
        "speciality": "Intelligence",
        "origin": "Germany"
    },
    "Labradoodle": {
        "name": "Labradoodle",
        "height": 55,
        "weight": 25,
        "breed": "Hybrid (Labrador Retriever + Poodle)",
        "purpose": "Companion",
        "speciality": "Hypoallergenic coat",
        "origin": "Australia"
    },
    "Puggle": {
        "name": "Puggle",
        "height": 30,
        "weight": 10,
        "breed": "Hybrid (Pug + Beagle)",
        "purpose": "Companion",
        "speciality": "Playful nature",
        "origin": "United States"
    },
    "Goldendoodle": {
        "name": "Goldendoodle",
        "height": 60,
        "weight": 30,
        "breed": "Hybrid (Golden Retriever + Poodle)",
        "purpose": "Companion",
        "speciality": "Friendly and sociable",
        "origin": "United States"
    },
    "Cockapoo": {
        "name": "Cockapoo",
        "height": 35,
        "weight": 10,
        "breed": "Hybrid (Cocker Spaniel + Poodle)",
        "purpose": "Companion",
        "speciality": "Affectionate",
        "origin": "United States"
    },
    "Pomsky": {
        "name": "Pomsky",
        "height": 38,
        "weight": 12,
        "breed": "Hybrid (Pomeranian + Husky)",
        "purpose": "Companion",
        "speciality": "Energetic",
        "origin": "United States"
    },
    "Schnoodle": {
        "name": "Schnoodle",
        "height": 50,
        "weight": 20,
        "breed": "Hybrid (Schnauzer + Poodle)",
        "purpose": "Companion",
        "speciality": "Loyal",
        "origin": "United States"
    },
    "Chorkie": {
        "name": "Chorkie",
        "height": 23,
        "weight": 4,
        "breed": "Hybrid (Chihuahua + Yorkshire Terrier)",
        "purpose": "Companion",
        "speciality": "Bold personality",
        "origin": "United States"
    },
    "Shih Poo": {
        "name": "Shih Poo",
        "height": 28,
        "weight": 6,
        "breed": "Hybrid (Shih Tzu + Poodle)",
        "purpose": "Companion",
        "speciality": "Friendly",
        "origin": "United States"
    },
    "Chiweenie": {
        "name": "Chiweenie",
        "height": 25,
        "weight": 5,
        "breed": "Hybrid (Chihuahua + Dachshund)",
        "purpose": "Companion",
        "speciality": "Lively",
        "origin": "United States"
    },
    "Maltipoo": {
        "name": "Maltipoo",
        "height": 30,
        "weight": 5,
        "breed": "Hybrid (Maltese + Poodle)",
        "purpose": "Companion",
        "speciality": "Gentle",
        "origin": "United States"
    },
    "Peekapoo": {
        "name": "Peekapoo",
        "height": 25,
        "weight": 4,
        "breed": "Hybrid (Pekingese + Poodle)",
        "purpose": "Companion",
        "speciality": "Affectionate",
        "origin": "United States"
    },
    "Beagle": {
        "name": "Beagle",
        "height": 40,
        "weight": 11,
        "breed": "Pure",
        "purpose": "Hunting",
        "speciality": "Good sense of smell",
        "origin": "England"
    },
    "Poodle": {
        "name": "Poodle",
        "height": 45,
        "weight": 22,
        "breed": "Pure",
        "purpose": "Companion",
        "speciality": "Intelligent",
        "origin": "Germany"
    },
    "Cocker Spaniel": {
        "name": "Cocker Spaniel",
        "height": 38,
        "weight": 12,
        "breed": "Pure",
        "purpose": "Hunting",
        "speciality": "Loyal",
        "origin": "England"
    },
    "Dachshund": {
        "name": "Dachshund",
        "height": 22,
        "weight": 9,
        "breed": "Pure",
        "purpose": "Hunting",
        "speciality": "Brave",
        "origin": "Germany"
    },
    "Husky": {
        "name": "Husky",
        "height": 60,
        "weight": 27,
        "breed": "Pure",
        "purpose": "Working",
        "speciality": "Strong",
        "origin": "Siberia"
    },
    "Maltese": {
        "name": "Maltese",
        "height": 20,
        "weight": 4,
        "breed": "Pure",
        "purpose": "Companion",
        "speciality": "Gentle",
        "origin": "Malta"
    },
    "Pomeranian": {
        "name": "Pomeranian",
        "height": 20,
        "weight": 3,
        "breed": "Pure",
        "purpose": "Companion",
        "speciality": "Lively",
        "origin": "Germany"
    },
    "Chihuahua": {
        "name": "Chihuahua",
        "height": 18,
        "weight": 2.5,
        "breed": "Pure",
        "purpose": "Companion",
        "speciality": "Bold",
        "origin": "Mexico"
    },
    "Yorkshire Terrier": {
        "name": "Yorkshire Terrier",
        "height": 20,
        "weight": 3,
        "breed": "Pure",
        "purpose": "Companion",
        "speciality": "Bold",
        "origin": "England"
    },
    "Shih Tzu": {
        "name": "Shih Tzu",
        "height": 28,
        "weight": 6,
        "breed": "Pure",
        "purpose": "Companion",
        "speciality": "Affectionate",
        "origin": "China"
    },
    "Dalmatian": {
        "name": "Dalmatian",
        "height": 58,
        "weight": 24,
        "breed": "Pure",
        "purpose": "Companion",
        "speciality": "Energetic",
        "origin": "Croatia"
    },
    "Great Dane": {
        "name": "Great Dane",
        "height": 80,
        "weight": 54,
        "breed": "Pure",
        "purpose": "Working",
        "speciality": "Gentle giant",
        "origin": "Germany"
    }
}
