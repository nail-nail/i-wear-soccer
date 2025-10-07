window.showToast = function showToast(title, message, type = "info", duration = 3200) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');

    if (!toastComponent || !toastTitle || !toastMessage || !toastIcon) {
        return;
    }

    const hiddenClasses = ['opacity-0', '-translate-y-6', 'pointer-events-none'];
    const visibleClasses = ['opacity-100', 'translate-y-0'];

    const typeKey = ['success', 'error', 'info'].includes(type) ? type : 'info';
    const icons = {
        success: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"></path></svg>',
        error: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><path d="M15 9 9 15"></path><path d="M9 9l6 6"></path></svg>',
        info: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>',
    };

    toastComponent.classList.remove('toast-success', 'toast-error', 'toast-info');
    toastComponent.classList.add(`toast-${typeKey}`);

    toastTitle.textContent = title;
    toastMessage.textContent = message;
    toastIcon.innerHTML = icons[typeKey];

    toastComponent.classList.remove(...hiddenClasses);
    toastComponent.classList.add(...visibleClasses);

    const previousTimeoutId = toastComponent.dataset.timeoutId;
    if (previousTimeoutId) {
        clearTimeout(Number(previousTimeoutId));
    }

    const timeoutId = window.setTimeout(() => {
        toastComponent.classList.remove(...visibleClasses);
        toastComponent.classList.add(...hiddenClasses);
    }, duration);

    toastComponent.dataset.timeoutId = String(timeoutId);
};
