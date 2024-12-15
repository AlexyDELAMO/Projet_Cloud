from main import app, db, Quiz, Question  # Assurez-vous d'importer aussi l'instance de l'app

# Créer la base de données et les tables dans le contexte de l'application
with app.app_context():
    db.create_all()


    quizzes = [
        {
            "title": "General Knowledge",
            "description": "Test your general knowledge with these questions.",
            "questions": [
                {"question_text": "What is the largest planet in our solar system?", 
                 "options": "Jupiter,Saturn,Earth,Mars", 
                 "correct_answer": "Jupiter"
                },
                {"question_text": "Which country has the most population in the world?", 
                 "options": "India,China,USA,Indonesia", 
                 "correct_answer": "China"
                },
                {"question_text": "What is the capital of Japan?", 
                 "options": "Tokyo,Kyoto,Osaka,Nagoya", 
                 "correct_answer": "Tokyo"
                },
                {"question_text": "Who wrote the play Romeo and Juliet?", 
                 "options": "William Shakespeare,Charles Dickens,Jane Austen,Leo Tolstoy", 
                 "correct_answer": "William Shakespeare"
                },
                {"question_text": "What is the boiling point of water at sea level?", 
                 "options": "100°C,90°C,110°C,80°C", 
                 "correct_answer": "100°C"
                },
                {"question_text": "Which continent is known as the 'Dark Continent'?", 
                 "options": "Africa,Asia,Europe,South America", 
                 "correct_answer": "Africa"
                },
                {"question_text": "Who painted the Mona Lisa?", 
                 "options": "Leonardo da Vinci,Vincent van Gogh,Pablo Picasso,Claude Monet", 
                 "correct_answer": "Leonardo da Vinci"
                },
                {"question_text": "What is the chemical formula of salt?", 
                 "options": "NaCl,H2O,CO2,KCl", 
                 "correct_answer": "NaCl"
                },
                {"question_text": "Which planet is known as the Red Planet?", 
                 "options": "Mars,Venus,Jupiter,Mercury", 
                 "correct_answer": "Mars"
                },
                {"question_text": "Which language is the most spoken worldwide?", 
                 "options": "English,Spanish,Mandarin,Hindi", 
                 "correct_answer": "Mandarin"
                }
            ]
        },
        {
            "title": "Science Trivia",
            "description": "Test your knowledge of science.",
            "questions": [
                {"question_text": "What is the powerhouse of the cell?", 
                 "options": "Nucleus,Mitochondria,Ribosome,Cytoplasm", 
                 "correct_answer": "Mitochondria"
                },
                {"question_text": "What gas do plants primarily absorb for photosynthesis?", 
                 "options": "Oxygen,Nitrogen,Carbon Dioxide,Hydrogen", 
                 "correct_answer": "Carbon Dioxide"
                },
                {"question_text": "What is the standard unit of electric current?", 
                 "options": "Ampere,Volt,Watt,Ohm", 
                 "correct_answer": "Ampere"
                },
                {"question_text": "What is the hardest natural substance on Earth?", 
                 "options": "Diamond,Graphite,Quartz,Gold", 
                 "correct_answer": "Diamond"
                },
                {"question_text": "Which part of the brain controls balance?", 
                 "options": "Cerebrum,Cerebellum,Medulla,Thalamus", 
                 "correct_answer": "Cerebellum"
                },
                {"question_text": "What is the primary gas in Earth's atmosphere?", 
                 "options": "Nitrogen,Oxygen,Carbon Dioxide,Argon", 
                 "correct_answer": "Nitrogen"
                },
                {"question_text": "What is the SI unit of force?", 
                 "options": "Joule,Newton,Pascal,Watt", 
                 "correct_answer": "Newton"
                },
                {"question_text": "What planet is closest to the Sun?", 
                 "options": "Mercury,Venus,Earth,Mars", 
                 "correct_answer": "Mercury"
                },
                {"question_text": "What is the process by which a liquid turns into a gas?", 
                 "options": "Condensation,Evaporation,Sublimation,Freezing", 
                 "correct_answer": "Evaporation"
                },
                {"question_text": "What is the pH of pure water?", 
                 "options": "5,7,9,10", 
                 "correct_answer": "7"
                },
                {
                    "question_text": "What is the chemical symbol for iron?",
                    "options": "Fe,I,Ir,F",
                    "correct_answer": "Fe"
                },
                {
                    "question_text": "Which scientist is known for the laws of motion?",
                    "options": "Isaac Newton,Albert Einstein,Galileo Galilei,Marie Curie",
                    "correct_answer": "Isaac Newton"
                },
                {
                    "question_text": "What is the most abundant element in the universe?",
                    "options": "Hydrogen,Oxygen,Helium,Carbon",
                    "correct_answer": "Hydrogen"
                },
                {
                    "question_text": "What part of the cell contains genetic material?",
                    "options": "Nucleus,Mitochondria,Ribosome,Cytoplasm",
                    "correct_answer": "Nucleus"
                },
                {
                    "question_text": "What is the process called when plants release oxygen?",
                    "options": "Photosynthesis,Respiration,Transpiration,Osmosis",
                    "correct_answer": "Photosynthesis"
                }
            ]
        },
        {
            "title": "Pop Culture",
            "description": "A fun quiz about movies, music, and trends.",
            "questions": [
                {"question_text": "Who directed the Lord of the Rings trilogy?", 
                 "options": "Peter Jackson,Steven Spielberg,James Cameron,George Lucas", 
                 "correct_answer": "Peter Jackson"
                },
                {"question_text": "What year did the first Harry Potter movie come out?", 
                 "options": "1999,2000,2001,2002", 
                 "correct_answer": "2001"
                },
                {"question_text": "Which artist released the album 1989?", 
                 "options": "Taylor Swift,Adele,Beyoncé,Rihanna", 
                 "correct_answer": "Taylor Swift"
                },
                {"question_text": "What TV show is known for the quote 'Winter is coming'?", 
                 "options": "Game of Thrones,Vikings,Breaking Bad,The Witcher", 
                 "correct_answer": "Game of Thrones"
                },
                {"question_text": "What is the name of the main character in The Legend of Zelda?", 
                 "options": "Zelda,Link,Ganon,Navi", 
                 "correct_answer": "Link"
                },
                {"question_text": "Who performed at the 2022 Super Bowl Halftime Show?", 
                 "options": "Eminem,Dr. Dre,Snoop Dogg,All of the above", 
                 "correct_answer": "All of the above"
                },
                {"question_text": "What movie is the song My Heart Will Go On associated with?", 
                 "options": "Titanic,The Notebook,Avatar,Moulin Rouge", 
                 "correct_answer": "Titanic"
                },
                {"question_text": "Who played Iron Man in the Marvel Cinematic Universe?", 
                 "options": "Chris Evans,Robert Downey Jr.,Chris Hemsworth,Mark Ruffalo", 
                 "correct_answer": "Robert Downey Jr."
                },
                {"question_text": "Which social media platform launched in 2010?", 
                 "options": "Instagram,Twitter,Snapchat,TikTok", 
                 "correct_answer": "Instagram"
                },
                {"question_text": "What is the name of the coffee shop in Friends?", 
                 "options": "Central Perk,The Coffee Bean,Java Jive,Brew House", 
                 "correct_answer": "Central Perk"
                },
                {
                    "question_text": "Who played Jack Sparrow in the Pirates of the Caribbean movies?",
                    "options": "Johnny Depp,Orlando Bloom,Keira Knightley,Geoffrey Rush",
                    "correct_answer": "Johnny Depp"
                },
                {
                    "question_text": "Which band is known for the song 'Bohemian Rhapsody'?",
                    "options": "Queen,The Beatles,Rolling Stones,Pink Floyd",
                    "correct_answer": "Queen"
                },
                {
                    "question_text": "What year did the Marvel Cinematic Universe start with Iron Man?",
                    "options": "2007,2008,2009,2010",
                    "correct_answer": "2008"
                },
                {
                    "question_text": "Which animated film features the character Simba?",
                    "options": "The Lion King,Tarzan,Frozen,Moana",
                    "correct_answer": "The Lion King"
                },
                {
                    "question_text": "What is the name of Taylor Swift's re-recorded version of her 2012 album?",
                    "options": "Red (Taylor's Version),Fearless (Taylor's Version),Speak Now (Taylor's Version),1989 (Taylor's Version)",
                    "correct_answer": "Red (Taylor's Version)"
                },
                {
                    "question_text": "Who won the first season of American Idol?",
                    "options": "Kelly Clarkson,Justin Guarini,Carrie Underwood,Clay Aiken",
                    "correct_answer": "Kelly Clarkson"
                },
                {
                    "question_text": "In which city is the sitcom Seinfeld primarily set?",
                    "options": "New York City,Los Angeles,Chicago,Boston",
                    "correct_answer": "New York City"
                },
                {
                    "question_text": "Who directed the movie *Inception*?",
                    "options": "Christopher Nolan,Quentin Tarantino,Steven Spielberg,James Cameron",
                    "correct_answer": "Christopher Nolan"
                },
                {
                    "question_text": "What is the name of the dragon in The Hobbit?",
                    "options": "Smaug,Drogon,Toothless,Falkor",
                    "correct_answer": "Smaug"
                },
                {
                    "question_text": "Which rapper released the song *God's Plan*?",
                    "options": "Drake,Eminem,Kanye West,Kendrick Lamar",
                    "correct_answer": "Drake"
                }

            ]
        }
    ]
    # Insertion des quiz et des questions dans la base de données
    for quiz_data in quizzes:
        # Créer un quiz
        quiz = Quiz(title=quiz_data["title"], description=quiz_data["description"])
        db.session.add(quiz)
        db.session.commit()  # Commit pour obtenir l'id du quiz

        # Ajouter les questions pour chaque quiz
        for question_data in quiz_data["questions"]:
            question = Question(
                question_text=question_data["question_text"],
                options=question_data["options"],
                correct_answer=question_data["correct_answer"],
                quiz_id=quiz.id
            )
            db.session.add(question)

        db.session.commit()

    print("Base de données initialisée avec succès !")
