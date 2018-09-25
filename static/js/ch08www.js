$(document).load = dis_input;

function dis_input() {
    var dis_input_display = document.getElementById('dis_input');
    if (dis_input_display.style.display === "block") {
        dis_input_display.style.display = 'none';
    }
    else if (dis_input_display.style.display === "none") {
        dis_input_display.style.display = 'block';
    }
}