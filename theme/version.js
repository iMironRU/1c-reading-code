document.addEventListener('DOMContentLoaded', function() {
    var footer = document.querySelector('.nav-wrapper') || document.body;
    var versionBadge = document.createElement('div');
    versionBadge.style.cssText = 'text-align:center;padding:8px;font-size:0.8em;opacity:0.6;';
    versionBadge.innerHTML = 'Версия <strong>v0.9.0</strong> · rev b17f380 · <a href="../CHANGELOG.md">Что изменилось</a>';
    document.body.appendChild(versionBadge);
});
