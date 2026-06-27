<script>
    export let title = "MODULE";
    export let glow = "cyan"; // cyan, orange, red
</script>

<div class="hud-card" style="--glow-color: var(--neon-{glow})">
    <div class="card-header">
        <span class="header-text">{title}</span>
        <div class="header-line"></div>
    </div>
    <div class="card-content">
        <slot />
    </div>

    <!-- Decorative corner markers -->
    <div class="corner top-left"></div>
    <div class="corner top-right"></div>
    <div class="corner bottom-left"></div>
    <div class="corner bottom-right"></div>
</div>

<style>
    .hud-card {
        position: relative;
        background: var(--bg-panel);
        border: 1px solid rgba(0, 243, 255, 0.1);
        padding: 1rem;
        backdrop-filter: blur(4px);
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
        display: flex;
        flex-direction: column;
        height: 100%;
        transition: all 0.3s ease;
    }

    .hud-card:hover {
        border-color: var(--glow-color);
        box-shadow:
            0 0 15px rgba(0, 243, 255, 0.1),
            inset 0 0 20px rgba(0, 243, 255, 0.05);
    }

    .card-header {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-size: 0.8rem;
        color: var(--glow-color);
        font-weight: bold;
        text-shadow: 0 0 5px var(--glow-color);
    }

    .header-line {
        flex-grow: 1;
        height: 1px;
        background: linear-gradient(90deg, var(--glow-color), transparent);
        margin-left: 10px;
        opacity: 0.5;
    }

    .card-content {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    /* Decorative Corners */
    .corner {
        position: absolute;
        width: 6px;
        height: 6px;
        border: 1px solid var(--glow-color);
        transition: all 0.3s ease;
    }

    .top-left {
        top: -1px;
        left: -1px;
        border-right: none;
        border-bottom: none;
    }
    .top-right {
        top: -1px;
        right: -1px;
        border-left: none;
        border-bottom: none;
    }
    .bottom-left {
        bottom: -1px;
        left: -1px;
        border-right: none;
        border-top: none;
    }
    .bottom-right {
        bottom: -1px;
        right: -1px;
        border-left: none;
        border-top: none;
    }
</style>
