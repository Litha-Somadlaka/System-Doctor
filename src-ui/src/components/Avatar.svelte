<script>
    export let status = "idle"; // idle, active, warning, critical

    $: colorVar =
        status === "critical"
            ? "var(--neon-red)"
            : status === "warning"
              ? "var(--neon-orange)"
              : "var(--neon-cyan)";
</script>

<div class="avatar-container" style="--avatar-color: {colorVar}">
    <div class="hologram-ring outer"></div>
    <div class="hologram-ring inner"></div>
    <div class="core-icon">
        <!-- Simple geometric tech shape -->
        <svg
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="1.5"
        >
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" />
        </svg>
    </div>
    <div class="status-text">{status.toUpperCase()}</div>
</div>

<style>
    .avatar-container {
        position: relative;
        width: 100px;
        height: 100px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 auto;
        color: var(--avatar-color);
    }

    .hologram-ring {
        position: absolute;
        border: 1px solid var(--avatar-color);
        border-radius: 50%;
        opacity: 0.6;
        box-shadow: 0 0 10px var(--avatar-color);
    }

    .outer {
        width: 100%;
        height: 100%;
        border-left-color: transparent;
        border-right-color: transparent;
        animation: spin 4s linear infinite;
    }

    .inner {
        width: 70%;
        height: 70%;
        border-top-color: transparent;
        border-bottom-color: transparent;
        animation: spin-reverse 3s linear infinite;
    }

    .core-icon {
        width: 40px;
        height: 40px;
        filter: drop-shadow(0 0 5px var(--avatar-color));
        animation: pulse 2s ease-in-out infinite;
    }

    .status-text {
        position: absolute;
        bottom: -20px;
        font-size: 0.6rem;
        letter-spacing: 2px;
        opacity: 0.8;
        white-space: nowrap;
    }

    @keyframes spin {
        from {
            transform: rotate(0deg);
        }
        to {
            transform: rotate(360deg);
        }
    }

    @keyframes spin-reverse {
        from {
            transform: rotate(360deg);
        }
        to {
            transform: rotate(0deg);
        }
    }

    @keyframes pulse {
        0%,
        100% {
            opacity: 0.8;
            transform: scale(1);
        }
        50% {
            opacity: 1;
            transform: scale(1.1);
        }
    }
</style>
