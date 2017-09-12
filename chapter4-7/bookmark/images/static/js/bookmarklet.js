(function(){
    var jquery_version = '2.1.4';
    var site_url = 'http://127.0.0.1:8000';
    var static_url = site_url + 'static/';
    var min_width = 100;
    var min_height = 100;

    function bookmarklet(msg) {
        var css = jQuery('<link>');
        css.attr({
            rel: 'sty;esheet',
            type: 'text/css',
            href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random() * 99999999999999999999999999)
        });

        jQuery('head').append(css);


        box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>Select an image to bookmark:</h1><div class="images"></div></div>';
        jQuery('body').append(box_html);

        jQuery('#bookmarklet #close').click(function(){
            jQuery('#bookmarklet').remove();
        });

        jQuery.each(jQuery('img[src$="jpg"]'), function(index, image){
            if (jQuery(image).width() >= min_width && jQuery(image).height() >= min_height){
                image_url = jQuery(image).attr('src');
                jQuery('#bookmarklet .images').append('Hello<a href="#"><img src="' + image_url +'" /></a>');
            }
        });

        jQuery('#bookmarklet .imags a').click(function(e){
            selected_image = jQuery(this).children('img').attr('src');

            jQuery('#bookmarklet').hide();

            window.open(site_url + 'images/create/?url=' + encodeURLComponent(selected_image) + '&title=' + encodeURLComponent(jQuery('title').text()), '_blank');
        });
    };


    // Check jquery is load or not
    if (typeof window.jQuery != 'undefined') {
        bookmarklet();
    }else{
        // check for conflicts
        var conflict = typeof window.$ != 'undefined';

        // create the script and point to Googole API
        var script = document.createElement('script');
        // script.setAttribute('src', 'http://apps.bdimg.com/libs/jquery/' + jquery_version + '/jquery.min.js');
        script.setAttribute('src', 'http://127.0.0.1:8000/static/js/jquery-3.1.1.min.js');

        document.getElementsByTagName('head')[0].appendChild(script);

        var attempts = 15;

        (function(){
            if (typeof window.jQuery == 'undefined'){
                if (--attempts > 0){
                    window.setTimeout(arguments.callee, 250)
                }else{
                    alert('An error ocurred while loading jQuery')
                }
            }else{
                bookmarklet();
            }
        })();
    }
})()
