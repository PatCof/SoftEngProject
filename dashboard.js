// JavaScript code to control the visibility and text color of courses

const activeCourses = document.getElementById('activeCourses');
const inactiveCourses = document.getElementById('inactiveCourses');
const activeButton = document.getElementById('activeButton');
const inactiveButton = document.getElementById('inactiveButton');

function toggleCourses(type) {
    if (type === 'active') {
        activeCourses.style.display = 'block';
        inactiveCourses.style.display = 'none';
        activeButton.classList.add('active');
        inactiveButton.classList.remove('active');
        // Set text color
        activeButton.style.color = 'black';
        inactiveButton.style.color = '#828282';
    } else if (type === 'inactive') {
        activeCourses.style.display = 'none';
        inactiveCourses.style.display = 'block';
        activeButton.classList.remove('active');
        inactiveButton.classList.add('active');
        // Set text color
        activeButton.style.color = '#828282';
        inactiveButton.style.color = 'black';
    }
}

// Add a click event listener to all announcements
const announcements = document.querySelectorAll('.announcement');

announcements.forEach((announcement) => {
    announcement.addEventListener('click', () => {
        // Perform an action when an announcement is clicked
        alert('You clicked on an announcement: ' + announcement.querySelector('.announcement-title').textContent);
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const addCourseButton = document.getElementById("addCourseButton");
  
    // Add an onclick event handler to the button
    addCourseButton.addEventListener("click", function() {
      // Navigate to another HTML page
      window.location.href = "addcourse.html";
    });
  });

  document.addEventListener("DOMContentLoaded", function () {
    const courseCreationForm = document.getElementById("courseCreationForm");

    courseCreationForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Get form inputs
        const courseName = document.getElementById("courseName").value;
        const courseDescription = document.getElementById("courseDescription").value;
        const startDate = document.getElementById("startDate").value;
        const endDate = document.getElementById("endDate").value;
        const labTimeDay = document.getElementById("labTimeDay").value;
        const lectureTimeDay = document.getElementById("lectureTimeDay").value;
        const courseImage = document.getElementById("courseImage").files[0];

        // Perform basic form validation
        if (!courseName || !courseDescription || !startDate || !endDate || !labTimeDay || !lectureTimeDay || !courseImage) {
            alert("Please fill in all fields.");
            return;
        }

        // You can now proceed with form submission or further processing
        // For example, you can use AJAX to send data to the server

        // Reset the form after successful submission
        courseCreationForm.reset();

        // Optionally, you can display a success message to the user
        alert("Course created successfully!");
    });
});
function discardCourse() {
    // Display a confirmation dialog
    var confirmDiscard = confirm("Are you sure you want to discard this course?");

    // If the user confirms, navigate to dashboard.html
    if (confirmDiscard) {
        window.location.href = "dashboard.html";
    }
}
function navigateToPostAnnouncement() {
    // Redirect to postannouncement.html
    window.location.href = "postannouncement.html";
}

// Initial state
toggleCourses('active'); // Set 'Active Courses' as the default
