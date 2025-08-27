import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Week Verdeler",
    page_icon="📅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide the Streamlit menu and footer
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# The Week Verdeler HTML code
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Week Verdeler</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #8D6E63;    /* Warm brown */
            --accent-color: #FF7043;     /* Warm orange */
            --background-color: #EFEBE9; /* Warm off-white */
            --first-half: #FFF8E1;       /* Soft cream */
            --wednesday: #B2DFDB;        /* Soft teal */
            --second-half: #FFE0B2;      /* Soft peach */
            --text-color: #4E342E;       /* Deep brown */
            --text-secondary: #5D4037;   /* Medium brown */
            --shadow-color: rgba(78, 52, 46, 0.15);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Quicksand', sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background-color: var(--background-color);
            color: var(--text-color);
            text-align: center;
            line-height: 1.6;
        }

        h1 {
            color: var(--primary-color);
            font-size: 2.5em;
            margin-bottom: 30px;
            text-shadow: 1px 1px 2px var(--shadow-color);
        }

        h2 {
            color: var(--text-secondary);
            font-size: 1.8em;
            margin-bottom: 15px;
            font-weight: 600;
        }

        h3 {
            color: var(--text-secondary);
            font-size: 1.4em;
            margin-bottom: 25px;
            font-weight: 500;
        }

        .announcement {
            font-size: 1.6em;
            margin: 25px 0;
            color: var(--accent-color);
            font-weight: 600;
        }

        .countdown {
            font-size: 1.4em;
            margin: 20px auto;
            padding: 12px 15px;
            background-color: var(--wednesday);
            border-radius: 10px;
            color: var(--text-secondary);
            font-weight: 500;
            max-width: 90%;
            box-shadow: 0 3px 6px var(--shadow-color);
        }

        .week-container {
            display: flex;
            margin: 40px auto;
            position: relative;
            border: none;
            box-shadow: 0 6px 12px var(--shadow-color);
            border-radius: 15px;
            overflow: hidden;
            height: 180px;
            perspective: 1000px;
            max-width: 100%;
        }

        .day {
            flex: 1;
            height: 100%;
            border-right: 1px solid rgba(78, 52, 46, 0.1);
            text-align: center;
            padding: 15px 5px;
            transition: all 1.5s;
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: relative;
            transform-origin: center left;
        }

        .day:last-child {
            border-right: none;
        }

        .first-half {
            background-color: var(--first-half);
        }

        .second-half {
            background-color: var(--second-half);
        }

        .wednesday {
            background-color: var(--wednesday);
        }

        .today {
            border-bottom: 4px solid var(--accent-color);
            box-shadow: inset 0 0 20px rgba(78, 52, 46, 0.1);
        }

        .day-name {
            font-weight: 700;
            font-size: 1.2em;
            margin-bottom: 15px;
            color: var(--text-color);
        }

        .day-date {
            font-size: 1em;
            color: var(--text-secondary);
        }

        .divider {
            position: absolute;
            left: 50%;
            top: -20px;
            bottom: -20px;
            width: 4px;
            background-color: var(--accent-color);
            display: none;
            z-index: 10;
            box-shadow: 0 0 10px var(--accent-color);
        }

        .divider-text {
            position: absolute;
            left: 47%;
            top: -45px;
            color: var(--accent-color);
            font-weight: 600;
            font-size: 1.2em;
            display: none;
            text-shadow: 1px 1px 2px var(--shadow-color);
        }

        button {
            display: block;
            margin: 30px auto;
            padding: 12px 30px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            font-size: 1.1em;
            font-weight: 600;
            font-family: 'Quicksand', sans-serif;
            box-shadow: 0 4px 8px var(--shadow-color);
            transition: all 0.3s ease;
        }

        button:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px var(--shadow-color);
            background-color: #795548;
        }

        button:active {
            transform: translateY(1px);
            box-shadow: 0 2px 5px var(--shadow-color);
        }

        #success-message {
            color: #558B2F;
            margin: 25px auto;
            font-weight: 600;
            font-size: 1.2em;
            background-color: rgba(185, 246, 202, 0.3);
            padding: 10px 20px;
            border-radius: 8px;
            max-width: 80%;
            box-shadow: 0 2px 6px var(--shadow-color);
        }

        .explosion {
            position: absolute;
            width: 50px;
            height: 50px;
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><polygon points="50,0 61,35 97,35 68,57 79,91 50,70 21,91 32,57 3,35 39,35" fill="%23FF7043"/></svg>');
            background-size: contain;
            background-repeat: no-repeat;
            z-index: 100;
            animation: explode 0.5s ease-out;
            display: none;
        }

        @keyframes explode {
            0% { transform: scale(0.1); opacity: 0; }
            70% { transform: scale(1.5); opacity: 1; }
            100% { transform: scale(1); opacity: 0; }
        }

        /* Mobile responsiveness */
        @media (max-width: 768px) {
            body {
                padding: 15px;
            }

            h1 {
                font-size: 2em;
            }

            h2 {
                font-size: 1.5em;
            }

            h3 {
                font-size: 1.2em;
            }

            .announcement {
                font-size: 1.3em;
            }

            .countdown {
                font-size: 1.1em;
            }

            .week-container {
                height: 150px;
            }

            .day-name {
                font-size: 0.9em;
                margin-bottom: 8px;
            }

            .day-date {
                font-size: 0.8em;
            }
        }

        @media (max-width: 480px) {
            .week-container {
                height: 120px;
            }

            .day {
                padding: 5px 2px;
            }

            .day-name {
                font-size: 0.8em;
                margin-bottom: 5px;
            }

            .day-date {
                font-size: 0.7em;
            }

            button {
                padding: 10px 20px;
                font-size: 1em;
            }

            .divider-text {
                font-size: 0.9em;
                left: 43%;
            }
        }
    </style>
</head>
<body>
    <h1>Week Verdeler</h1>
    <h2 id="current-date">Vandaag is...</h2>
    <h3 id="week-half">We zijn in de...</h3>
    
    <div class="countdown" id="countdown">Nog ... dagen tot de volgende verdeling</div>
    
    <div class="announcement" id="wednesday-message"></div>

    <div class="week-container" id="week-display">
        <div class="divider" id="divider"></div>
        <div class="divider-text" id="divider-text">Week Verdeler</div>
        <!-- Days will be inserted here by JavaScript -->
    </div>

    <div id="explosions"></div>

    <button id="divide-btn">Toon Week Verdeling Animatie</button>
    <div id="success-message" style="display: none;">
        Week succesvol in twee helften verdeeld!
    </div>

    <script>
        // Dutch translations
        const weekdayNamesDutch = ["Zondag", "Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag"];
        const monthNamesDutch = ["Januari", "Februari", "Maart", "April", "Mei", "Juni", "Juli", "Augustus", "September", "Oktober", "November", "December"];
        
        // Get current date information
        const today = new Date();
        const currentWeekday = today.getDay(); // 0 is Sunday, 6 is Saturday
        
        // Calculate the start of the week (Sunday)
        const startOfWeek = new Date(today);
        startOfWeek.setDate(today.getDate() - today.getDay());
        
        // Update date display
        document.getElementById('current-date').textContent = `Vandaag is ${weekdayNamesDutch[currentWeekday]}, ${today.getDate()} ${monthNamesDutch[today.getMonth()]} ${today.getFullYear()}`;
        
        // Determine which half of the week we're in
        let half;
        if (currentWeekday < 3) { // Sunday(0), Monday(1), Tuesday(2)
            half = "Eerste Helft";
        } else if (currentWeekday === 3) { // Wednesday
            half = "Overgangsdag (Woensdag)";
        } else { // Thursday(4), Friday(5), Saturday(6)
            half = "Tweede Helft";
        }
        document.getElementById('week-half').textContent = `We zijn in de ${half} van de week`;
        
        // Calculate days until next Wednesday
        function daysUntilNextWednesday() {
            let daysUntil = (3 - currentWeekday + 7) % 7;
            if (daysUntil === 0) daysUntil = 7; // If today is Wednesday, count to next Wednesday
            return daysUntil;
        }
        
        // Display countdown
        const daysToWednesday = daysUntilNextWednesday();
        let countdownText;
        if (currentWeekday === 3) {
            countdownText = "Vandaag is de verdeling!";
        } else if (daysToWednesday === 1) {
            countdownText = "Nog 1 dag tot de volgende verdeling";
        } else {
            countdownText = `Nog ${daysToWednesday} dagen tot de volgende verdeling`;
        }
        document.getElementById('countdown').textContent = countdownText;
        
        // If it's Wednesday, show special message
        if (currentWeekday === 3) {
            document.getElementById('wednesday-message').textContent = "Woensdag verdeelt de week in tweeën!";
        }
        
        // Create week display
        const weekDisplay = document.getElementById('week-display');
        for (let i = 0; i < 7; i++) {
            const dayDate = new Date(startOfWeek);
            dayDate.setDate(startOfWeek.getDate() + i);
            
            const dayElement = document.createElement('div');
            dayElement.className = 'day';
            
            // Add appropriate class based on which half and if it's today
            if (i === currentWeekday) {
                dayElement.classList.add('today');
            }
            
            if (i === 3) { // Wednesday
                dayElement.classList.add('wednesday');
            } else if (i < 3) { // First half
                dayElement.classList.add('first-half');
            } else { // Second half
                dayElement.classList.add('second-half');
            }
            
            // Add day content
            const dayNameElement = document.createElement('div');
            dayNameElement.className = 'day-name';
            dayNameElement.textContent = weekdayNamesDutch[i];
            dayElement.appendChild(dayNameElement);
            
            const dayDateElement = document.createElement('div');
            dayDateElement.className = 'day-date';
            dayDateElement.textContent = `${dayDate.getDate()} ${monthNamesDutch[dayDate.getMonth()].substring(0, 3)}`;
            dayElement.appendChild(dayDateElement);
            
            weekDisplay.appendChild(dayElement);
        }
        
        // Create explosion effect
        function createExplosion(x, y) {
            const explosionsContainer = document.getElementById('explosions');
            const explosion = document.createElement('div');
            explosion.className = 'explosion';
            explosion.style.left = `${x}px`;
            explosion.style.top = `${y}px`;
            explosion.style.display = 'block';
            explosionsContainer.appendChild(explosion);
            
            // Remove explosion after animation
            setTimeout(() => {
                explosion.remove();
            }, 500);
        }
        
        // Animation function
        function animateDivision() {
            const divider = document.getElementById('divider');
            const dividerText = document.getElementById('divider-text');
            const days = document.querySelectorAll('.day');
            const successMessage = document.getElementById('success-message');
            const weekContainer = document.getElementById('week-display');
            const containerRect = weekContainer.getBoundingClientRect();
            
            // Show divider
            divider.style.display = 'block';
            dividerText.style.display = 'block';
            
            // Create multiple explosions along the dividing line
            for (let i = 0; i < 5; i++) {
                setTimeout(() => {
                    const y = containerRect.top + 20 + i * 40;
                    createExplosion(containerRect.left + containerRect.width/2, y);
                }, i * 200);
            }
            
            // Animate first half days (they fold or collapse)
            for (let i = 0; i < 3; i++) {
                days[i].style.transform = 'rotateY(30deg) scale(0.9)';
                days[i].style.opacity = '0.7';
                days[i].style.filter = 'blur(1px)';
            }
            
            // Animate Wednesday
            days[3].style.transform = 'scale(1.05)';
            days[3].style.boxShadow = '0 0 15px rgba(0,0,0,0.2)';
            days[3].style.zIndex = '5';
            
            // Animate second half days (they move right)
            for (let i = 4; i < 7; i++) {
                days[i].style.transform = 'translateX(60px)';
            }
            
            // Show success message after animation
            setTimeout(() => {
                successMessage.style.display = 'block';
            }, 1500);
        }
        
        // Set up button handler
        document.getElementById('divide-btn').addEventListener('click', animateDivision);
        
        // Auto-animate if it's Wednesday
        if (currentWeekday === 3) {
            setTimeout(animateDivision, 1000);
        }
    </script>
</body>
</html>
"""

# Display the HTML app using Streamlit's components
components.html(html_code, height=700, scrolling=False)

# Optional: Add a small footer
st.markdown("""
<div style="text-align: center; color: #8D6E63; margin-top: 20px; font-size: 0.8em;">
    Made with ❤️ for Mama
</div>
""", unsafe_allow_html=True)
