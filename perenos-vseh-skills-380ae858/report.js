(() => {
  const data = window.REPORT_DATA || { items: [], meta: {} };
  const items = data.items;
  const search = document.getElementById('search');
  const kind = document.getElementById('kind-filter');
  const status = document.getElementById('status-filter');
  const rows = document.getElementById('report-rows');
  const empty = document.getElementById('empty-result');
  const count = document.getElementById('result-count');

  const setText = (id, value) => {
    const element = document.getElementById(id);
    if (element) element.textContent = String(value);
  };

  setText('report-lead', data.meta.lead || 'Полный реестр адаптированных компонентов.');
  setText('audio-transcript', data.meta.audioText || 'Голосовой итог будет добавлен после проверки.');
  setText('fact-total', items.length);
  setText('fact-installed', items.filter(item => item.installed).length);
  setText('fact-skills', items.filter(item => item.kind === 'skill').length);
  setText('fact-agents', items.filter(item => item.kind === 'agent').length);
  if (data.meta.checks) setText('checks-summary', data.meta.checks);

  const cell = (tag, text, className) => {
    const element = document.createElement(tag);
    element.textContent = text;
    if (className) element.className = className;
    return element;
  };

  const badgeFor = item => {
    if (item.integration) return ['badge badge-integration', 'Интеграция'];
    return item.installed ? ['badge badge-installed', 'Установлен'] : ['badge badge-adapt', 'Ожидает'];
  };

  const render = () => {
    const query = search.value.trim().toLocaleLowerCase('ru');
    const filtered = items.filter(item => {
      const haystack = `${item.name} ${item.description} ${item.direction}`.toLocaleLowerCase('ru');
      const queryMatch = !query || haystack.includes(query);
      const kindMatch = kind.value === 'all' || item.kind === kind.value;
      const statusMatch = status.value === 'all'
        || (status.value === 'installed' && item.installed)
        || (status.value === 'pending' && !item.installed)
        || (status.value === 'integration' && item.integration);
      return queryMatch && kindMatch && statusMatch;
    });

    rows.replaceChildren();
    filtered.forEach(item => {
      const row = document.createElement('tr');
      row.appendChild(cell('th', item.name, 'cell-name')).scope = 'row';
      row.appendChild(cell('td', item.kind === 'agent' ? 'Бывший агент' : 'Скилл'));
      row.appendChild(cell('td', item.direction || 'Без категории'));
      const [badgeClass, badgeText] = badgeFor(item);
      row.appendChild(cell('td', badgeText, badgeClass));
      row.appendChild(cell('td', item.description));
      row.appendChild(cell('td', item.integration ? 'Требуется отдельная настройка' : 'Не требуется'));
      rows.appendChild(row);
    });
    count.textContent = `Показано ${filtered.length} из ${items.length}`;
    empty.hidden = filtered.length !== 0;
  };

  [search, kind, status].forEach(control => control.addEventListener('input', render));
  document.getElementById('reset-filters').addEventListener('click', () => {
    search.value = '';
    kind.value = 'all';
    status.value = 'all';
    render();
    search.focus();
  });
  render();
})();
