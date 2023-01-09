const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 400
})

sr.reveal(`.sticky-header`, {delay: 500});
sr.reveal(`.rev-slider`, {delay: 800, origin: 'bottom'});
sr.reveal(`.mission_vision`, {delay: 1000, origin: 'left'});
sr.reveal(`.principal_img`, {delay: 600, origin: 'left'});
sr.reveal(`.principal_msg`, {delay: 700, origin: 'right'});
sr.reveal(`.principal_title`, {delay: 500, origin: 'top'});
sr.reveal(`.event-titls`, {delay: 500, origin: 'top'});
sr.reveal(`.upcoming-event-carousel`, {delay: 600, origin: 'bottom'});