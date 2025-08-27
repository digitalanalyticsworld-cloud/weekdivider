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
            transition: all 1.8s ease-in-out;
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

        /* No CSS positioning for saw/divider - will be positioned in JS */
        .divider {
            position: absolute;
            top: -20px;
            bottom: -20px;
            width: 4px;
            background-color: var(--accent-color);
            display: none;
            z-index: 5;
            box-shadow: 0 0 10px var(--accent-color);
        }

        .divider-text {
            position: absolute;
            top: -45px;
            color: var(--accent-color);
            font-weight: 600;
            font-size: 1.2em;
            display: none;
            text-shadow: 1px 1px 2px var(--shadow-color);
        }
        
        /* Saw styles */
        .saw-container {
            position: absolute;
            top: -60px;
            width: 40px;
            height: 300px;
            transform: translateX(-50%);
            z-index: 20;
            display: none;
        }
        
        .saw-handle {
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 20px;
            height: 60px;
            background-color: #5D4037;
            border-radius: 4px;
        }
        
        .saw-blade {
            position: absolute;
            top: 60px;
            left: 50%;
            transform: translateX(-50%);
            width: 40px;
            height: 200px;
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 200"><path d="M20,0 L30,10 L20,20 L30,30 L20,40 L30,50 L20,60 L30,70 L20,80 L30,90 L20,100 L30,110 L20,120 L30,130 L20,140 L30,150 L20,160 L30,170 L20,180 L30,190 L20,200 L10,190 L20,180 L10,170 L20,160 L10,150 L20,140 L10,130 L20,120 L10,110 L20,100 L10,90 L20,80 L10,70 L20,60 L10,50 L20,40 L10,30 L20,20 L10,10 Z" fill="silver" stroke="%235D4037" stroke-width="1" /></svg>');
            background-repeat: no-repeat;
        }

        .saw-dust {
            position: absolute;
            width: 8px;
            height: 8px;
            background-color: #D7CCC8;
            border-radius: 50%;
            opacity: 0.9;
            z-index: 15;
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
        
        button:disabled {
            background-color: #BCAAA4;
            transform: none;
            cursor: not-allowed;
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
        
        @keyframes sawDust {
            0% { transform: translateY(-5px); opacity: 1; }
            100% { transform: translateY(50px) rotate(180deg); opacity: 0; }
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
            
            .saw-container {
                width: 30px;
            }
            
            .saw-handle {
                width: 15px;
                height: 40px;
            }
            
            .saw-blade {
                top: 40px;
                width: 30px;
                height: 150px;
                background-size: 30px 150px;
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
        
        <!-- Saw Element -->
        <div class="saw-container" id="saw">
            <div class="saw-handle"></div>
            <div class="saw-blade"></div>
        </div>
        
        <!-- Days will be inserted here by JavaScript -->
    </div>

    <div id="sawdust-container"></div>
    <div id="explosions"></div>

    <button id="divide-btn">Zaag De Week Doormidden!</button>
    <div id="success-message" style="display: none;">
        Week succesvol in twee helften gezaagd!
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
            dayElement.id = `day-${i}`;  // Add ID for easier targeting
            
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
        
        // Create sawdust effect
        function createSawdust(x, y) {
            const sawdustContainer = document.getElementById('sawdust-container');
            const sawdust = document.createElement('div');
            sawdust.className = 'saw-dust';
            
            // Randomize position slightly
            const offsetX = (Math.random() - 0.5) * 20;
            
            sawdust.style.left = `${x + offsetX}px`;
            sawdust.style.top = `${y}px`;
            sawdustContainer.appendChild(sawdust);
            
            // Create animation
            sawdust.style.animation = `sawDust ${0.5 + Math.random() * 0.5}s ease-out`;
            
            // Remove after animation
            setTimeout(() => {
                sawdust.remove();
            }, 1000);
        }
        
        // Animation function
        function animateDivision() {
            const divider = document.getElementById('divider');
            const dividerText = document.getElementById('divider-text');
            const days = document.querySelectorAll('.day');
            const successMessage = document.getElementById('success-message');
            const weekContainer = document.getElementById('week-display');
            const containerRect = weekContainer.getBoundingClientRect();
            const saw = document.getElementById('saw');
            const wednesdayElement = document.getElementById('day-3'); // Wednesday has ID day-3
            const wednesdayRect = wednesdayElement.getBoundingClientRect();
            
            // Calculate the center of Wednesday
            const wednesdayCenter = wednesdayRect.left + (wednesdayRect.width / 2);
            
            // Position the saw and divider at the center of Wednesday
            saw.style.left = `${wednesdayCenter}px`;
            divider.style.left = `${wednesdayCenter}px`;
            dividerText.style.left = `${wednesdayCenter - 60}px`;
            
            // Disable button during animation
            document.getElementById('divide-btn').disabled = true;
            
            // Show divider
            divider.style.display = 'block';
            dividerText.style.display = 'block';
            
            // Show saw
            saw.style.display = 'block';
            
            // Saw cutting animation
            let sawPosition = 0;
            let goingDown = true;
            
            const sawAnimation = setInterval(() => {
                if (goingDown) {
                    sawPosition += 5;
                    if (sawPosition >= containerRect.height) {
                        goingDown = false;
                    }
                } else {
                    sawPosition -= 5;
                    if (sawPosition <= 0) {
                        goingDown = true;
                    }
                }
                
                // Create sawdust at current position
                createSawdust(wednesdayCenter, containerRect.top + sawPosition);
                
                // Move saw
                saw.style.top = `${sawPosition - 60}px`;
                
            }, 50);
            
            // Split animation effect after a delay
            setTimeout(() => {
                // Create a visual slit in Wednesday
                const slit = document.createElement('div');
                slit.style.position = 'absolute';
                slit.style.top = '0';
                slit.style.bottom = '0';
                slit.style.width = '4px';
                slit.style.left = '50%';
                slit.style.transform = 'translateX(-50%)';
                slit.style.backgroundColor = 'rgba(255, 87, 34, 0.5)';
                slit.style.zIndex = '10';
                wednesdayElement.style.position = 'relative';
                wednesdayElement.style.overflow = 'visible';
                wednesdayElement.appendChild(slit);
                
                // CHANGED: Move first half days (Sun-Tue) more out of view
                for (let i = 0; i < 3; i++) {
                    days[i].style.transform = 'translateX(-120px)';
                    days[i].style.opacity = '0.6';
                }
                
                // Animate Wednesday halves
                const leftContent = wednesdayElement.innerHTML;
                wednesdayElement.innerHTML = '';
                
                const leftHalf = document.createElement('div');
                leftHalf.style.position = 'absolute';
                leftHalf.style.left = '0';
                leftHalf.style.top = '0';
                leftHalf.style.width = '50%';
                leftHalf.style.height = '100%';
                leftHalf.style.background = 'var(--wednesday)';
                leftHalf.style.transition = 'transform 1.8s ease-in-out';
                leftHalf.style.overflow = 'hidden';
                leftHalf.style.borderTopLeftRadius = '10px';
                leftHalf.style.borderBottomLeftRadius = '10px';
                leftHalf.innerHTML = leftContent;
                leftHalf.style.display = 'flex';
                leftHalf.style.flexDirection = 'column';
                leftHalf.style.justifyContent = 'center';
                leftHalf.style.transform = 'translateX(-60px)';
                leftHalf.style.opacity = '0.75';
                
                const rightHalf = document.createElement('div');
                rightHalf.style.position = 'absolute';
                rightHalf.style.left = '50%';
                rightHalf.style.top = '0';
                rightHalf.style.width = '50%';
                rightHalf.style.height = '100%';
                rightHalf.style.background = 'var(--wednesday)';
                rightHalf.style.transition = 'transform 1.8s ease-in-out';
                rightHalf.style.overflow = 'hidden';
                rightHalf.style.borderTopRightRadius = '10px';
                rightHalf.style.borderBottomRightRadius = '10px';
                rightHalf.innerHTML = leftContent;
                rightHalf.style.display = 'flex';
                rightHalf.style.flexDirection = 'column';
                rightHalf.style.justifyContent = 'center';
                rightHalf.style.transform = 'translateX(20px)';
                
                wednesdayElement.appendChild(leftHalf);
                wednesdayElement.appendChild(rightHalf);
                wednesdayElement.appendChild(slit);
                
                // CHANGED: Keep second half (Thu-Sat) more visible and prominent
                const weekWidth = containerRect.width;
                const dayWidth = weekWidth / 7;
                
                // Center the second half of the week (Thu-Sat) by moving them left
                for (let i = 4; i < 7; i++) {
                    days[i].style.transform = 'translateX(-40px)';
                    days[i].style.opacity = '1';
                    days[i].style.boxShadow = '0 5px 15px rgba(0,0,0,0.1)';
                    days[i].style.zIndex = '2';
                }
            }, 2000);
            
            // Stop saw animation and show success after cutting is done
            setTimeout(() => {
                clearInterval(sawAnimation);
                
                // Hide saw
                saw.style.display = 'none';
                
                // Show success message
                successMessage.style.display = 'block';
                
                // Re-enable button
                document.getElementById('divide-btn').disabled = false;
            }, 4000);
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
