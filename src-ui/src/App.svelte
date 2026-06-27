<script>
  import Card from "./components/Card.svelte";
  import Gauge from "./components/Gauge.svelte";
  import Avatar from "./components/Avatar.svelte";
  import { onMount } from "svelte";

  let cpu = 15;
  let ram = 42;
  let disk = 65;
  let network = "ONLINE";

  // Mock processes
  let processes = [
    { name: "chrome.exe", mem: "450 MB", glow: false },
    { name: "code.exe", mem: "320 MB", glow: false },
    { name: "python.exe", mem: "120 MB", glow: false },
    { name: "spotify.exe", mem: "95 MB", glow: false },
    { name: "system", mem: "45 MB", glow: false },
  ];

  // Simulation loop
  onMount(() => {
    const interval = setInterval(() => {
      // Fluctuate values slightly for "alive" feel
      cpu = Math.max(5, Math.min(100, cpu + (Math.random() * 10 - 5)));
      ram = Math.max(20, Math.min(90, ram + (Math.random() * 6 - 3)));

      // Shuffle processes occasionally
      if (Math.random() > 0.8) {
        processes[0].mem = Math.floor(400 + Math.random() * 100) + " MB";
        processes = [...processes];
      }
    }, 2000);

    return () => clearInterval(interval);
  });

  function handleBoost() {
    alert("SYSTEM OPTIMIZATION SEQUENCE INITIATED...");
    // Future IPC call here
  }
</script>

<main class="hud-container">
  <!-- HEADER / TOP BAR -->
  <header class="hud-header">
    <div class="logo">SYSTEM DOCTOR <span class="version">v1.0</span></div>
    <div class="status-indicators">
      <div class="indicator active">NET: {network}</div>
      <div class="indicator">SECURE</div>
    </div>
  </header>

  <!-- MAIN GRID -->
  <div class="hud-grid">
    <!-- LEFT COLUMN: AVATAR & ACTIONS -->
    <div class="col-left">
      <Card title="AI ASSISTANT" glow="cyan">
        <div class="avatar-wrapper">
          <Avatar />
        </div>
        <div class="message-log">
          <p>> System nominal.</p>
          <p>> Monitoring active.</p>
        </div>
      </Card>

      <div class="action-area">
        <button class="boost-btn" on:click={handleBoost}>
          <span class="btn-text">BOOST SYSTEM</span>
          <div class="btn-glare"></div>
        </button>
      </div>
    </div>

    <!-- MIDDLE COLUMN: METRICS -->
    <div class="col-center">
      <div class="metrics-row">
        <Card title="CPU CORE" glow={cpu > 80 ? "red" : "cyan"}>
          <Gauge value={cpu} label="LOAD" color={cpu > 80 ? "red" : "cyan"} />
        </Card>
        <Card title="MEMORY" glow={ram > 70 ? "orange" : "cyan"}>
          <Gauge
            value={ram}
            label="USED"
            color={ram > 70 ? "orange" : "cyan"}
          />
        </Card>
      </div>

      <Card title="VIRTUAL STORAGE" glow="blue">
        <div class="disk-bar-container">
          <div class="disk-label">
            <span>C:\ DRIVE</span>
            <span>{Math.round(disk)}%</span>
          </div>
          <div class="progress-bar-bg">
            <div class="progress-bar-fill" style="width: {disk}%"></div>
          </div>
        </div>
      </Card>
    </div>

    <!-- RIGHT COLUMN: PROCESSES -->
    <div class="col-right">
      <Card title="TOP PROCESSES" glow="orange">
        <ul class="process-list">
          {#each processes as proc}
            <li class="process-item">
              <span class="proc-name">{proc.name}</span>
              <span class="proc-mem">{proc.mem}</span>
            </li>
          {/each}
        </ul>
      </Card>
    </div>
  </div>
</main>

<style>
  .hud-container {
    height: 100vh;
    display: flex;
    flex-direction: column;
    padding: 1rem;
    box-sizing: border-box;
    gap: 1rem;
  }

  .hud-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(0, 243, 255, 0.2);
    padding-bottom: 0.5rem;
  }

  .logo {
    font-size: 1.2rem;
    font-weight: bold;
    letter-spacing: 4px;
    color: var(--neon-cyan);
    text-shadow: 0 0 10px var(--neon-cyan);
  }

  .version {
    font-size: 0.6rem;
    color: var(--text-dim);
    vertical-align: top;
  }

  .status-indicators {
    display: flex;
    gap: 1rem;
    font-size: 0.7rem;
    color: var(--text-dim);
  }

  .indicator.active {
    color: var(--neon-cyan);
    text-shadow: 0 0 5px var(--neon-cyan);
  }

  /* GRID LAYOUT */
  .hud-grid {
    display: grid;
    grid-template-columns: 250px 1fr 250px;
    gap: 1rem;
    flex-grow: 1;
  }

  /* COLUMN SPECIFICS */
  .col-left {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .col-center {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .metrics-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    flex-grow: 1;
  }

  .col-right {
    display: flex;
    flex-direction: column;
  }

  /* AVATAR & LOG */
  .avatar-wrapper {
    flex-grow: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1rem 0;
  }

  .message-log {
    font-size: 0.7rem;
    color: var(--text-dim);
    font-family: monospace;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    padding-top: 0.5rem;
  }

  .message-log p {
    margin: 2px 0;
  }

  /* BOOST BUTTON */
  .action-area {
    margin-top: auto;
  }

  .boost-btn {
    width: 100%;
    padding: 1rem;
    background: transparent;
    border: 1px solid var(--neon-cyan);
    color: var(--neon-cyan);
    font-size: 1rem;
    letter-spacing: 2px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: all 0.3s;
    text-shadow: 0 0 5px var(--neon-cyan);
    box-shadow: 0 0 10px rgba(0, 243, 255, 0.1);
  }

  .boost-btn:hover {
    background: rgba(0, 243, 255, 0.1);
    box-shadow: 0 0 20px rgba(0, 243, 255, 0.4);
    transform: translateY(-2px);
  }

  .boost-btn:active {
    transform: translateY(1px);
  }

  /* DISK BARS */
  .disk-bar-container {
    padding: 1rem;
  }

  .disk-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.8rem;
    margin-bottom: 5px;
    color: var(--neon-blue);
  }

  .progress-bar-bg {
    height: 6px;
    background: rgba(255, 255, 255, 0.1);
    width: 100%;
    position: relative;
  }

  .progress-bar-fill {
    height: 100%;
    background: var(--neon-blue);
    position: absolute;
    top: 0;
    left: 0;
    box-shadow: 0 0 10px var(--neon-blue);
    transition: width 1s ease;
  }

  /* PROCESS LIST */
  .process-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .process-item {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    font-size: 0.8rem;
  }

  .proc-name {
    color: var(--text-main);
  }

  .proc-mem {
    color: var(--neon-orange);
    font-family: monospace;
  }
</style>
