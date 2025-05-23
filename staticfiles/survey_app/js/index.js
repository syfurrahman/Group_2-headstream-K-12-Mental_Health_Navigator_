// Mobile Navigation Toggle
const mobileToggle = document.querySelector('.mobile-toggle');
const navLinks = document.querySelector('.nav-links');

mobileToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Close mobile menu when clicking a link
const navItems = document.querySelectorAll('.nav-links a');
navItems.forEach(item => {
    item.addEventListener('click', () => {
        navLinks.classList.remove('active');
    });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 70,
                behavior: 'smooth'
            });
        }
    });
});

const chatModal = document.getElementById("chatModal");
const floatingChatButton = document.getElementById("floatingChatButton");
const closeChat = document.getElementById("closeChat");
const chatBody = document.getElementById("chatBody");
const chatInput = document.getElementById("chatInput");
const sendMessageButton = document.getElementById("sendMessage");
const initialPrompt = document.getElementById("initialPrompt");

let messages = [];

function toggleChat() {
  chatModal.classList.toggle("hidden");
}

function renderMessages() {
  chatBody.innerHTML = "";
  if (messages.length === 0) {
    chatBody.appendChild(initialPrompt);
  } else {
    messages.forEach(msg => {
      const div = document.createElement("div");
      div.className = msg.sender === "user" ? "user-msg" : "bot-msg";
      if (msg.sender === "user") {
        // Prevent user HTML injection
        div.textContent = msg.text;
      } else {
        // Allow bot to render safe HTML (like links)
        div.innerHTML = DOMPurify.sanitize(msg.text);
      }
      chatBody.appendChild(div);
    });
  }
}

async function sendMessage() {
  const input = chatInput.value.trim();
  if (!input) return;

  const userMessage = { sender: "user", text: input };
  messages.push(userMessage);
  chatInput.value = "";
  renderMessages();

  try {
    const res = await fetch(`${window.location.origin}/chat/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });

    const data = await res.json();
    const botMessage = { sender: "groq", text: data.reply };
    messages.push(botMessage);
  } catch (err) {
    console.error(err);
    messages.push({ sender: "groq", text: "Oops! Something went wrong." });
  }

  renderMessages();
}

floatingChatButton.addEventListener("click", toggleChat);
closeChat.addEventListener("click", toggleChat);
sendMessageButton.addEventListener("click", sendMessage);
chatInput.addEventListener("keydown", e => {
  if (e.key === "Enter") sendMessage();
});



document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.querySelector(".dropdown-toggle");
    const dropdown = toggle.closest(".dropdown");

    toggle.addEventListener("click", function (e) {
        e.preventDefault(); // Prevent the default anchor behavior
        dropdown.classList.toggle("open");
    });

    // Optional: click outside to close
    document.addEventListener("click", function (e) {
        if (!dropdown.contains(e.target)) {
            dropdown.classList.remove("open");
        }
    });
});


  // Simple JavaScript for interactive elements
  document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            if (targetId) {
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 100,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
    
    // Mobile navigation toggle
    const createMobileMenu = () => {
        const nav = document.querySelector('nav');
        const header = document.querySelector('header');
        
        const menuToggle = document.createElement('button');
        menuToggle.textContent = '☰ Menu';
        menuToggle.classList.add('mobile-menu-toggle');
        menuToggle.style.display = 'none';
        menuToggle.style.padding = '10px 15px';
        menuToggle.style.background = '#0066cc';
        menuToggle.style.color = '#fff';
        menuToggle.style.border = 'none';
        menuToggle.style.borderRadius = '4px';
        menuToggle.style.cursor = 'pointer';
        menuToggle.style.marginTop = '10px';
        
        header.querySelector('.logo-container').after(menuToggle);
        
        menuToggle.addEventListener('click', () => {
            nav.style.display = nav.style.display === 'block' ? 'none' : 'block';
        });
        
        const updateMenu = () => {
            if (window.innerWidth <= 768) {
                menuToggle.style.display = 'block';
                nav.style.display = 'none';
            } else {
                menuToggle.style.display = 'none';
                nav.style.display = 'block';
            }
        };
        
        window.addEventListener('resize', updateMenu);
        updateMenu();
    };
    
    createMobileMenu();
    
    // Add active class to current page in navigation
    const currentPage = window.location.pathname.split('/').pop();
    document.querySelectorAll('nav ul li a').forEach(link => {
        if (link.getAttribute('href').indexOf(currentPage) !== -1) {
            link.style.color = '#0066cc';
            link.style.fontWeight = '700';
        }
    });
});


/*******************************************************
 * WARNING: DO NOT MODIFY THE CODE BELOW
 * This code is critical for the functionality of the application.
 * Modifying this code will cause unexpected behavior or break features.
 *******************************************************/
// Modal for Survey Form
// Modal for Survey Form
// Modal for Survey Form
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('surveyModal');
    const closeModal = document.getElementById('closeModal');
    const surveyContent = document.getElementById('surveyContent');

    const thankYouModal = document.getElementById('thankYouModal');
    const closeThankYouModal = document.getElementById('closeThankYouModal');

    let countdownInterval;

    // Function to show the survey modal
    function showModal() {
        modal.classList.add('active');
        modal.classList.remove('hidden');
    }

    // Function to hide the survey modal
    function hideModal() {
        modal.classList.remove('active');
        modal.classList.add('hidden');
        sessionStorage.setItem('surveyShown', 'true'); // Mark the survey as shown
    }

    // Function to show the thank you modal
    let topLinks = []; // Define topLinks globally

    // Function to show the thank you modal
    function showThankYouModal(topLinks) {
        const topLinksContainer = document.getElementById('topLinksContainer');

        thankYouModal.classList.add('active');
        thankYouModal.classList.remove('hidden');

        // Clear any existing content
        topLinksContainer.innerHTML = '';

        // Create the new layout for the top 5 links
        topLinks.forEach(link => {
            const linkBox = document.createElement('div');
            linkBox.classList.add('flashcard');

            // Set the content for the flashcard
            linkBox.innerHTML = `
                <div class="flashcard-banner">${link.title}</div>
                <div class="flashcard-body">${link.description}</div>
            `;

            // Add click event to open the link in a new tab
            linkBox.addEventListener('click', () => {
                window.open(link.url, '_blank'); // Open the link in a new tab
            });

            // Append the flashcard to the container
            topLinksContainer.appendChild(linkBox);
        });
    }

    // Function to hide the thank you modal
    function hideThankYouModal() {
        thankYouModal.classList.remove('active');
        thankYouModal.classList.add('hidden');
        clearInterval(countdownInterval); // Stop the countdown if the modal is closed
    }

    // Automatically load the survey form when the page loads
    function loadSurveyForm() {
        fetch('/survey/') // URL to the survey_form view
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to load survey form');
                }
                return response.text();
            })
            .then(html => {
                surveyContent.innerHTML = html; // Inject the HTML into the modal
                addCSRFToken(); // Add CSRF token to the form
                attachFormSubmitHandler(); // Attach the form submission handler
                initializeSurveyLogic(); // Initialize survey logic
                showModal(); // Show the modal
            })
            .catch(error => {
                console.error('Error loading survey form:', error);
            });
    }

    // Close the survey modal when the close button is clicked
    if (closeModal) {
        closeModal.addEventListener('click', hideModal);
    }

    // Close the thank you modal when the close button is clicked
    if (closeThankYouModal) {
        closeThankYouModal.addEventListener('click', hideThankYouModal);
    }

    // Check if the survey has already been shown in this session
    if (!sessionStorage.getItem('surveyShown')) {
        loadSurveyForm(); // Load and show the survey form
    }

    // Function to add CSRF token to the form
    function addCSRFToken() {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const form = surveyContent.querySelector('form');
        if (form) {
            const csrfInput = document.createElement('input');
            csrfInput.type = 'hidden';
            csrfInput.name = 'csrfmiddlewaretoken';
            csrfInput.value = csrfToken;
            form.appendChild(csrfInput);
        }
    }

    // Function to attach form submission handler
    function attachFormSubmitHandler() {
        const surveyForm = surveyContent.querySelector('form');
        if (!surveyForm) return;
    
        surveyForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // Prevent the default form submission
    
            const formData = new FormData(surveyForm);
    
            try {
                const response = await fetch('/modal-survey-submit/', {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': getCSRFToken(), // Include the CSRF token
                    },
                });
    
                const result = await response.json();
    
                if (result.success) {
                    // Hide the survey modal
                    hideModal();
    
                    // Show the thank you modal with the top links
                    showThankYouModal(result.top_links || []);
                } else {
                    alert(result.message || 'An error occurred while submitting the survey.');
                }
            } catch (error) {
                console.error('Error submitting the survey:', error);
                alert('An unexpected error occurred. Please try again.');
            }
        });
    }

    // Helper function to get the CSRF token
    function getCSRFToken() {
        const cookieValue = document.cookie
            .split('; ')
            .find(row => row.startsWith('csrftoken='))
            ?.split('=')[1];
        return cookieValue || '';
    }

    // Function to initialize survey logic
    function initializeSurveyLogic() {
        const surveyDataElement = document.getElementById('surveyData');
        if (!surveyDataElement) return;

        const surveyData = JSON.parse(surveyDataElement.textContent);
        console.log("Parsed survey data:", surveyData);

        const allQuestions = surveyData.questions;
        const openEndedQuestions = surveyData.openEndedQuestions;

        const questionMap = {};
        allQuestions.forEach(q => {
            questionMap[q.id] = q;
        });

        const openEndedMap = {};
        openEndedQuestions.forEach(q => {
            openEndedMap[q.id] = q;
        });

        const topContainer = document.getElementById('top-container');
        const bottomContainer = document.getElementById('bottom-container');

        function createMultipleChoiceBlock(question) {
            const block = document.createElement('div');
            block.classList.add('question-block');
            block.id = question.id;

            const p = document.createElement('p');
            p.innerHTML = `<strong>${question.text}</strong>`;
            block.appendChild(p);

            question.answers.forEach(answer => {
                const label = document.createElement('label');
                label.style.display = 'block';

                const input = document.createElement('input');
                input.type = 'radio';
                input.name = question.id;
                input.value = answer.text;

                label.appendChild(input);
                label.appendChild(document.createTextNode(' ' + answer.text));
                block.appendChild(label);
            });

            return block;
        }

        function createOpenEndedBlock(question) {
            const block = document.createElement('div');
            block.classList.add('question-block');
            block.id = question.id;

            const p = document.createElement('p');
            p.innerHTML = `<strong>${question.text}</strong>`;
            block.appendChild(p);

            const input = document.createElement('input');
            input.type = 'text';
            input.name = question.id;
            input.placeholder = question.placeholder || "Enter your response here...";
            input.style.width = '100%';
            block.appendChild(input);

            return block;
        }

        function showFollowUpQuestions(followUpQuestionIds) {
            followUpQuestionIds.forEach(questionId => {
                if (!document.getElementById(questionId)) {
                    const def = questionMap[questionId];
                    if (def) {
                        const block = createMultipleChoiceBlock(def);
                        topContainer.appendChild(block);

                        block.querySelectorAll('input[type="radio"]').forEach(radio => {
                            radio.addEventListener('change', event => {
                                const chosenText = event.target.value;
                                const chosenAnswer = def.answers.find(a => a.text === chosenText);
                                if (chosenAnswer && chosenAnswer.followUpQuestionId) {
                                    showFollowUpQuestions(chosenAnswer.followUpQuestionId);
                                }
                            });
                        });
                    }
                }
            });
        }

        const q1Def = questionMap['Q1'];
        if (q1Def) {
            const q1Block = createMultipleChoiceBlock(q1Def);
            topContainer.appendChild(q1Block);

            q1Block.querySelectorAll('input[type="radio"]').forEach(radio => {
                radio.addEventListener('change', event => {
                    ['Q2a', 'Q2b', 'Q3a', 'Q3b', 'Q3c'].forEach(id => removeIfExists(id));

                    const chosenText = event.target.value;
                    const chosenAnswer = q1Def.answers.find(a => a.text === chosenText);
                    if (chosenAnswer && chosenAnswer.followUpQuestionId) {
                        showFollowUpQuestions(chosenAnswer.followUpQuestionId);
                    }
                });
            });
        }

        function removeIfExists(id) {
            const el = document.getElementById(id);
            if (el) el.remove();
        }

        // Show standard questions (Q4, Q5, Q6, Q7, Q8)
        const q4Def = questionMap['Q4'];
        if (q4Def) {
            bottomContainer.appendChild(createMultipleChoiceBlock(q4Def));
        }
        const q5Def = questionMap['Q5'];
        if (q5Def) {
            bottomContainer.appendChild(createMultipleChoiceBlock(q5Def));
        }

        ['Q6', 'Q7', 'Q8'].forEach(oeId => {
            const def = openEndedMap[oeId];
            if (def) {
                bottomContainer.appendChild(createOpenEndedBlock(def));
            }
        });
    }
});
/*******************************************************
 * WARNING: DO NOT MODIFY THE CODE ABOVE
 * This code is critical for the functionality of the application.
 * Modifying this code will cause unexpected behavior or break features.
 *******************************************************/