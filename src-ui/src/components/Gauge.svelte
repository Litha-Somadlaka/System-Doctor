<script>
    export let value = 0; // 0 to 100
    export let label = "USAGE";
    export let color = "cyan"; // cyan, orange, red

    $: circumference = 2 * Math.PI * 40; // r=40
    $: offset = circumference - (value / 100) * circumference;
    $: strokeColor = `var(--neon-${color})`;
</script>

<div class="gauge-container">
    <svg class="progress-ring" width="120" height="120">
        <!-- Background Track -->
        <circle
            class="progress-ring__circle track"
            stroke="rgba(255,255,255,0.1)"
            stroke-width="8"
            fill="transparent"
            r="40"
            cx="60"
            cy="60"
        />
        <!-- Progress Arc -->
        <circle
            class="progress-ring__circle progress"
            stroke={strokeColor}
            stroke-width="8"
            stroke-dasharray={circumference}
            stroke-dashoffset={offset}
            stroke-linecap="round"
            fill="transparent"
            r="40"
            cx="60"
            cy="60"
        />
    </svg>

    <div class="gauge-value">
        <span class="number" style="color: {strokeColor}"
            >{Math.round(value)}%</span
        >
        <span class="label">{label}</span>
    </div>
</div>

<style>
    .gauge-container {
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 120px;
        height: 120px;
        margin: 0 auto;
    }

    .progress-ring__circle {
        transition:
            stroke-dashoffset 0.5s ease-out,
            stroke 0.3s ease;
        transform: rotate(-90deg);
        transform-origin: 50% 50%;
    }

    .progress {
        filter: drop-shadow(0 0 4px var(--glow-color));
    }

    .gauge-value {
        position: absolute;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    .number {
        font-size: 1.5rem;
        font-weight: bold;
        text-shadow: 0 0 10px currentColor;
    }

    .label {
        font-size: 0.6rem;
        color: var(--text-dim);
        letter-spacing: 1px;
        margin-top: 2px;
    }
</style>
