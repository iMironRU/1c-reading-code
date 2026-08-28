/* Песочница: кнопка «Запустить» у листингов, помеченных ```bsl,песочница
 *
 * Контракт ссылки — url-contract.md v1.0 в репозитории iMironRU/BSLexicon:
 *   ?code   листинг в URL-safe base64 (RFC 4648 §5, без padding)
 *   ?source адрес страницы книги — тренажёр покажет провенанс-баннер
 *   ?title  подпись в баннере
 *
 * Автозапуска нет намеренно: листинг может содержать бесконечный цикл,
 * читатель нажимает «Запустить» сам уже в тренажёре.
 *
 * mdBook отдаёт помеченный блок как <pre><code class="language-bsl песочница">.
 * Это единственная форма, которую разбирают оба сборщика: pandoc склеивает
 * строку в один класс, но в EPUB, PDF и DOCX листинг и должен остаться
 * листингом — там запускать нечего.
 */
(function () {
    'use strict';

    var TRAINER = 'https://imironru.github.io/BSLexicon/';

    function toBase64Url(text) {
        var bytes = new TextEncoder().encode(text);
        var bin = '';
        for (var i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
        return btoa(bin).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
    }

    /* Подпись баннера: «<Книга> — § N.M». Номер берём из заголовка страницы —
     * во всей серии он совпадает с именем файла, поэтому отдельного источника
     * для него не нужно. */
    function provenanceTitle() {
        var book = (document.querySelector('.menu-title') || {}).textContent || '';
        var h1 = document.querySelector('main h1');
        var section = '';
        if (h1) {
            var m = h1.textContent.match(/§\s*\d+\.\d+/);
            if (m) section = m[0].replace(/\s+/g, ' ');
        }
        book = book.trim();
        if (book && section) return book + ' — ' + section;
        return book || section || document.title;
    }

    function sandboxUrl(code) {
        var params = new URLSearchParams({ code: toBase64Url(code) });
        params.set('source', window.location.href.split('#')[0]);
        var title = provenanceTitle();
        if (title) params.set('title', title);
        return TRAINER + '?' + params.toString();
    }

    function decorate(codeEl) {
        var pre = codeEl.closest('pre');
        if (!pre || pre.parentElement.classList.contains('sandbox-block')) return;

        var wrap = document.createElement('div');
        wrap.className = 'sandbox-block';
        pre.parentNode.insertBefore(wrap, pre);
        wrap.appendChild(pre);

        var bar = document.createElement('div');
        bar.className = 'sandbox-bar';

        var link = document.createElement('a');
        link.className = 'sandbox-run';
        link.textContent = '▶ Запустить в песочнице';
        link.target = '_blank';
        link.rel = 'noopener noreferrer';
        /* Ссылку считаем на клике: код может подмениться подсветкой уже после
         * загрузки, а textContent на момент клика точно окончательный. */
        link.addEventListener('click', function () {
            link.href = sandboxUrl(codeEl.textContent.replace(/\n$/, ''));
        });
        link.href = '#';

        var note = document.createElement('span');
        note.className = 'sandbox-note';
        note.textContent = 'откроется в новой вкладке, код не запустится сам';

        bar.appendChild(link);
        bar.appendChild(note);
        wrap.appendChild(bar);
    }

    function init() {
        if (!window.TextEncoder || !window.URLSearchParams) return;
        document.querySelectorAll('code.песочница, code.sandbox').forEach(decorate);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
