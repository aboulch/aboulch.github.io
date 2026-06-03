function loadHeader() {
    fetch('header.html')
        .then(response => response.text())
        .then(data => {
            document.querySelector('header').innerHTML = data;
            const navSlide = () => {
                const burger = document.querySelector('.burger');
                const nav = document.querySelector('.nav-links');

                if (burger) {
                    burger.addEventListener('click', () => {
                        nav.classList.toggle('nav-active');
                    });
                }
            }
            navSlide();
        });
}

loadHeader();