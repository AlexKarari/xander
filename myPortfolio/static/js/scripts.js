/*============================================
	Skills
	==============================================*/
$('.skills-item').each(function () {
    var perc = $(this).find('.percent').data('percent');

    $(this).data('height', perc);
})

$('.touch .skills-item').each(function () {
    $(this).css({ 'height': $(this).data('height') + '%' });
})

$('.touch .skills-bars').css({ 'opacity': 1 });
