const galleryItems = document.querySelectorAll(".gallery-item");
const lightbox = document.querySelector(".lightbox");
const lightboxImg = document.querySelector("#lightbox-image");
const closeBtn = document.querySelector("#close-btn");

galleryItems.forEach((item) => {
  item.addEventListener("click", handleLightboxOpen);
});

closeBtn.addEventListener("click", handleLightboxClose);
lightbox.addEventListener("click", handleLightboxClose);

function handleLightboxOpen(event) {
  const src = event.target.src;
  lightbox.style.display = "flex";
  lightboxImg.src = src.replace("-thumbnail", "");
}

function handleLightboxClose(event) {
  lightbox.style.display = "none";
}
