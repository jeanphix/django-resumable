$(document).ready(function () {
    "use strict";
    $('input[upload-url]').each(function (index, el) {
        var r = new Resumable({
            target: $(el).attr('upload-url'),
            query: {
                'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val()
            }
        });
        if (r.support) {
            r.assignBrowse(el);
            var el = $(el);
            var progress = $('<progress value="0" max="1" />').css('display', 'none');
            var path_name = $(el).attr('name') + '-path';
            var path = $('[name=' + path_name + ']');
            var path_label = $('label[for=id_' + path_name + ']');
            el.after(progress);
            r.on('fileAdded', function () {
                r.upload();
                progress.css('display', 'inline');
            });
            r.on('progress', function () {
                progress.attr('value', r.progress());
            });
            r.on('fileSuccess', function (file) {
                path.attr('value', file.size + '_' + file.fileName);
                path_label.text('current: ' + file.fileName);
                progress.css('display', 'none');
            });
            el.parents('form').on('submit', function () {
                // Don't send the file on post.
                el.remove();
            });
        }
    });
});
