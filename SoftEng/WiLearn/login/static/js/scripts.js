
const images = ["static/images/image1.jpg",
                "static/images/image2.jpg",
                "static/images/image3.jpg"];
let currentIndex = 0;

function showImage() {
    const slideshowContainer = document.querySelector(".slideshow-container");
    slideshowContainer.innerHTML = ""; // Clear the container

    const img = document.createElement("img");
    img.src = images[currentIndex];
    img.alt = "Image " + (currentIndex + 1);

    slideshowContainer.appendChild(img);

    currentIndex = (currentIndex + 1) % images.length;
    setTimeout(showImage, 5000); // Change image every 3 seconds (adjust as needed)
}

showImage(); // Start the slideshow