document.addEventListener('DOMContentLoaded', function() {
    var textarea = document.getElementById('activities-textarea');
    var lines = textarea.innerHTML.split('\n');
    var coloredLines = [];
    for (var i = 0; i < lines.length; i++) {
        if (lines[i].startsWith('Earned')) {
            coloredLines.push('<div style="color: green;">' + lines[i] + '</div>');
        } else if (lines[i].startsWith('Entered')) {
            coloredLines.push('<div style="color: red;">' + lines[i] + '</div>');
        } else {
            coloredLines.push('<div style="color: blue;">' + lines[i] + '</div>');
        }
    }
    textarea.innerHTML = coloredLines.join('\n');
    textarea.scrollTop = textarea.scrollHeight;
});