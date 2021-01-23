window.addEventListener('scroll', () => {
    console.log(window.scrollY);
    localStorage.setItem('scrollY',window.scrollY);
}, false);

window.addEventListener('load', () => {
    const y = localStorage.getItem('scrollY');
    if (y) {
        document.documentElement.scrollTop = y;
    };
}, false);

const test = (type) => {
    document.getElementById(`add-${type}-container`).style.opacity = 1;
    document.getElementById(`add-${type}-container`).style.visibility = "visible";
}

const closeForm = (type) => {
    document.getElementById(`add-${type}-container`).style.opacity = 0;
    document.getElementById(`add-${type}-container`).style.visibility = "hidden";
}