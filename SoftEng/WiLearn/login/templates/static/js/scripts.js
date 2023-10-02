function toggleBackToTop() {
    const backToTop = document.getElementById("back-to-top");
    if (document.documentElement.scrollTop > window.innerHeight) {
        backToTop.style.display = "block";
    } else {
        backToTop.style.display = "none";
    }
}

// Function to scroll to the top of the page
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

// Attach event listeners
window.addEventListener("scroll", toggleBackToTop);
document.getElementById("back-to-top").addEventListener("click", scrollToTop);

// Image slideshow functionality
const images = ["static/images/image1.jpg",
                "static/images/image2.jpg",
                "static/images/image3.jpg"];
let currentIndex = 0;

function showImage() {
    const slideshowContainer = document.querySelector(".slideshow-container");
    const dotContainer = document.querySelector(".dot-container");

    // Clear the container and dots
    slideshowContainer.innerHTML = "";
    dotContainer.innerHTML = "";

    // Create and append the current image
    const img = document.createElement("img");
    img.src = images[currentIndex];
    img.alt = "Image " + (currentIndex + 1);
    slideshowContainer.appendChild(img);

    // Create and append navigation dots
    for (let i = 0; i < images.length; i++) {
        const dot = document.createElement("span");
        dot.className = "dot";
        dot.onclick = () => showSlide(i);
        dotContainer.appendChild(dot);
    }

    // Set the active class on the current dot
    const dots = document.querySelectorAll(".dot");
    dots[currentIndex].classList.add("active");

    currentIndex = (currentIndex + 1) % images.length;

    // Call the function recursively after a delay
    setTimeout(showImage, 5000); // Change image every 5 seconds (adjust as needed)
}

function showSlide(index) {
    currentIndex = index;
    showImage(); // Start displaying images from the selected index
}

// JavaScript function to open the login popup
function openLoginPopup() {
    var popup = document.getElementById('loginPopup');
    popup.style.display = 'block';
    document.body.classList.add('popup-open'); // Add the class
}

// JavaScript function to close the login popup
function closeLoginPopup() {
    var popup = document.getElementById('loginPopup');
    popup.style.display = 'none';
    document.body.classList.remove('popup-open'); // Remove the class
}

showImage();