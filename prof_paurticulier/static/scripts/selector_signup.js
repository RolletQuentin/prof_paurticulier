selector = document.getElementById("selection_signup");
output = document.getElementById("output_container");
signup = document.getElementById("signup");
bg_color = getComputedStyle(document.documentElement).getPropertyValue('--second-bg-color');


output.addEventListener("click", function (e) {
    if (e.target != signup) {
        selector.className = "";
        signup.style.backgroundColor = bg_color;
    } else {
        selector.className = "active";
        signup.style.backgroundColor = "rgb(140, 140, 230)";
    }

})