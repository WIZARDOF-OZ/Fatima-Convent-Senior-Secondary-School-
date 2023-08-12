const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 600
})

// sr.reveal(`#menuDropdown`, {delay: 3000});
sr.reveal(`.rev-slider`, {delay: 3000, origin: 'bottom'});
sr.reveal(`.mission_vision`, {delay: 1000, origin: 'left'});
sr.reveal(`.principal_img`, {delay: 600, origin: 'left'});
sr.reveal(`.principal_msg, .msg_1p`, {delay: 700, origin: 'right'});
sr.reveal(`.principal_title`, {delay: 500, origin: 'top'});
sr.reveal(`.event-titls`, {delay: 500, origin: 'top'});
sr.reveal(`.upcoming-event-carousel, .btn_event`, {delay: 600, origin: 'bottom'});