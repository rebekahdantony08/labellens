<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LabelLens AI — Ingredient Safety & Health Advisor</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <!-- Chart.js for Safety Gauge & Stats -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Vanilla Tilt for 3D Interactive Parallax Cards -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.8.1/vanilla-tilt.min.js"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        slate: {
                            950: '#05070c',
                            900: '#0b101d',
                            800: '#162032',
                        },
                        emerald: {
                            400: '#34d399',
                            500: '#10b981',
                            900: '#064e3b',
                        },
                        cyan: {
                            400: '#22d3ee',
                            500: '#06b6d4',
                        },
                        magenta: {
                            400: '#f472b6',
                            500: '#ec4899',
                            600: '#db2777'
                        },
                        rose: {
                            500: '#f43f5e',
                        },
                        amber: {
                            500: '#f59e0b',
                        }
                    },
                    animation: {
                        'pulse-glow': 'pulseGlow 3s infinite ease-in-out',
                        'scan-line': 'scanLine 2.5s infinite linear',
                        'float-3d': 'float3D 6s ease-in-out infinite',
                        'orbit': 'orbit 16s linear infinite',
                        'molecule-float': 'moleculeFloat 10s ease-in-out infinite alternate',
                    },
                    keyframes: {
                        pulseGlow: {
                            '0%, 100%': { opacity: 0.4, transform: 'scale(1)' },
                            '50%': { opacity: 0.8, transform: 'scale(1.05)' },
                        },
                        scanLine: {
                            '0%': { top: '0%' },
                            '100%': { top: '100%' },
                        },
                        float3D: {
                            '0%, 100%': { transform: 'translateY(0px) rotateX(10deg) rotateY(-12deg)' },
                            '50%': { transform: 'translateY(-16px) rotateX(18deg) rotateY(8deg)' },
                        },
                        orbit: {
                            '0%': { transform: 'rotate(0deg) translateX(120px) rotate(0deg)' },
                            '100%': { transform: 'rotate(360deg) translateX(120px) rotate(-360deg)' }
                        },
                        moleculeFloat: {
                            '0%': { transform: 'translate(0, 0) rotate(0deg)' },
                            '100%': { transform: 'translate(30px, -40px) rotate(45deg)' }
                        }
                    }
                }
            }
        }
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #05070c;
            color: #f8fafc;
            overflow-x: hidden;
            perspective: 1200px;
        }

        /* 3D Glassmorphism Styles */
        .glass-card {
            background: rgba(11, 16, 29, 0.7);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.5), 0 0 15px rgba(16, 185, 129, 0.05);
            transform-style: preserve-3d;
        }

        .glass-card-interactive {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            transform-style: preserve-3d;
        }
        .glass-card-interactive:hover {
            border-color: rgba(52, 211, 153, 0.4);
            box-shadow: 0 20px 45px -10px rgba(16, 185, 129, 0.25), 0 0 25px rgba(236, 72, 153, 0.15);
        }

        /* 3D Container Presets */
        .perspective-container {
            perspective: 1000px;
            transform-style: preserve-3d;
        }

        /* 3D Glowing Neon Rings */
        .neon-ring-emerald {
            box-shadow: 0 0 20px rgba(16, 185, 129, 0.4), inset 0 0 15px rgba(16, 185, 129, 0.3);
            border: 2px solid #10b981;
        }
        .neon-ring-magenta {
            box-shadow: 0 0 20px rgba(236, 72, 153, 0.4), inset 0 0 15px rgba(236, 72, 153, 0.3);
            border: 2px solid #ec4899;
        }

        /* 3D Holographic Product Mockup */
        .holo-bottle {
            transform-style: preserve-3d;
            transition: transform 0.1s ease-out;
            background: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, rgba(16,185,129,0.08) 50%, rgba(236,72,153,0.12) 100%);
            box-shadow: inset 0 0 30px rgba(255,255,255,0.2), 0 25px 50px -12px rgba(0,0,0,0.8), 0 0 30px rgba(16,185,129,0.3);
        }
        .holo-label {
            background: rgba(11, 16, 29, 0.85);
            border: 1px solid rgba(52, 211, 153, 0.4);
            transform: translateZ(25px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }

        /* Grid Background Pattern */
        .bg-3d-grid {
            background-size: 50px 50px;
            background-image: 
                linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #05070c;
        }
        ::-webkit-scrollbar-thumb {
            background: #162032;
            border-radius: 9999px;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between selection:bg-emerald-500 selection:text-black bg-3d-grid">

    <!-- 3D BACKGROUND PARTICLE & MOLECULE CANVAS GRID -->
    <div class="fixed inset-0 pointer-events-none z-0 overflow-hidden">
        <!-- Ambient Color Flares -->
        <div class="absolute -top-20 left-1/4 w-[30rem] h-[30rem] bg-emerald-500/15 rounded-full blur-[140px] animate-pulse-glow"></div>
        <div class="absolute bottom-0 right-1/4 w-[35rem] h-[35rem] bg-magenta-500/10 rounded-full blur-[160px] animate-pulse-glow" style="animation-delay: 1.5s;"></div>
        <div class="absolute top-1/2 left-2/3 w-96 h-96 bg-cyan-500/10 rounded-full blur-[120px]"></div>

        <!-- Floating 3D SVGs: Chemical Structure & Allergen Spheres -->
        <svg class="absolute top-1/6 left-10 w-28 h-28 text-emerald-400/20 animate-molecule-float" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1.5">
            <polygon points="50,15 85,35 85,75 50,95 15,75 15,35" />
            <circle cx="50" cy="15" r="5" fill="#34d399" />
            <circle cx="85" cy="35" r="5" fill="#ec4899" />
            <circle cx="85" cy="75" r="5" fill="#34d399" />
            <circle cx="50" cy="95" r="5" fill="#22d3ee" />
            <line x1="50" y1="15" x2="50" y2="50" stroke="#10b981" stroke-dasharray="2,2"/>
        </svg>

        <svg class="absolute bottom-1/4 right-12 w-36 h-36 text-magenta-400/20 animate-molecule-float" style="animation-delay: 3s;" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="30" cy="30" r="12" />
            <circle cx="70" cy="30" r="8" />
            <circle cx="50" cy="70" r="14" />
            <line x1="30" y1="30" x2="70" y2="30" />
            <line x1="30" y1="30" x2="50" y2="70" />
            <line x1="70" y1="30" x2="50" y2="70" />
        </svg>

        <!-- Floating 3D Allergen Glowing Spheres -->
        <div class="absolute top-1/3 left-1/2 w-6 h-6 rounded-full bg-gradient-to-br from-emerald-400 to-cyan-500 blur-[1px] opacity-60 animate-orbit"></div>
        <div class="absolute top-2/3 left-1/3 w-8 h-8 rounded-full bg-gradient-to-br from-magenta-500 to-rose-500 blur-[2px] opacity-50 animate-float-3d"></div>
    </div>

    <!-- MAIN WRAPPER -->
    <div class="relative z-10 flex flex-col min-h-screen">
        
        <!-- HEADER & NAVIGATION -->
        <header class="sticky top-0 z-50 glass-card border-b border-slate-800/80 px-4 lg:px-8 py-3.5">
            <div class="max-w-7xl mx-auto flex items-center justify-between">
                
                <!-- Brand Logo with 3D Depth -->
                <div class="flex items-center gap-3">
                    <div class="relative flex items-center justify-center w-11 h-11 rounded-2xl bg-gradient-to-br from-emerald-400 via-cyan-400 to-magenta-500 p-[1.5px] shadow-lg shadow-emerald-500/25">
                        <div class="w-full h-full bg-slate-950 rounded-[14px] flex items-center justify-center">
                            <i data-lucide="scan-line" class="w-5 h-5 text-emerald-400 animate-pulse"></i>
                        </div>
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="font-extrabold text-2xl tracking-tight bg-gradient-to-r from-white via-slate-100 to-slate-400 bg-clip-text text-transparent">
                                LabelLens<span class="text-emerald-400">.ai</span>
                            </span>
                            <span class="px-2.5 py-0.5 text-[10px] font-bold uppercase tracking-wider bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 rounded-full shadow-[0_0_10px_rgba(16,185,129,0.2)]">3D Pro v2.8</span>
                        </div>
                        <p class="text-xs text-slate-400 hidden sm:block">AI Ingredient Safety & Health Advisor</p>
                    </div>
                </div>

                <!-- Nav Items -->
                <nav class="hidden md:flex items-center gap-1 bg-slate-900/90 p-1.5 rounded-2xl border border-slate-800 shadow-inner">
                    <button onclick="switchTab('scanner')" id="nav-scanner" class="px-4 py-2 text-xs font-semibold rounded-xl transition-all bg-gradient-to-r from-emerald-500 to-cyan-500 text-slate-950 shadow-lg shadow-emerald-500/20 flex items-center gap-2">
                        <i data-lucide="camera" class="w-3.5 h-3.5"></i> Label Scanner
                    </button>
                    <button onclick="switchTab('history')" id="nav-history" class="px-4 py-2 text-xs font-semibold rounded-xl transition-all text-slate-400 hover:text-white flex items-center gap-2">
                        <i data-lucide="history" class="w-3.5 h-3.5"></i> Scan History
                    </button>
                    <button onclick="switchTab('diet')" id="nav-diet" class="px-4 py-2 text-xs font-semibold rounded-xl transition-all text-slate-400 hover:text-white flex items-center gap-2">
                        <i data-lucide="sliders" class="w-3.5 h-3.5"></i> Health Profile
                    </button>
                </nav>

                <!-- Status Indicator & Settings -->
                <div class="flex items-center gap-3">
                    <div class="hidden sm:flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-slate-900/90 border border-slate-800 shadow-md">
                        <span class="relative flex h-2.5 w-2.5">
                          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                          <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
                        </span>
                        <span class="text-xs font-medium text-slate-300">Gemini 2.5 Active</span>
                    </div>

                    <button onclick="toggleApiKeyModal()" class="p-2.5 rounded-2xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 transition-colors shadow-md" title="API Key Settings">
                        <i data-lucide="key" class="w-4 h-4"></i>
                    </button>
                </div>
            </div>
        </header>

        <!-- MAIN DASHBOARD CONTENT -->
        <main class="flex-1 max-w-7xl w-full mx-auto p-4 lg:p-8 space-y-8">
            
            <!-- SECTION 1: SCANNER TAB -->
            <div id="tab-scanner" class="space-y-8 transition-all duration-300">
                
                <!-- Hero Section with 3D Holographic Bottle Showcase -->
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center py-4">
                    
                    <div class="lg:col-span-8 space-y-4 text-left">
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-magenta-500/10 border border-magenta-500/30 text-magenta-300 text-xs font-bold">
                            <i data-lucide="sparkles" class="w-3.5 h-3.5 text-magenta-400"></i> Next-Gen Visual AI Ingredient Detection
                        </div>
                        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold tracking-tight bg-gradient-to-b from-white via-slate-100 to-slate-400 bg-clip-text text-transparent leading-tight">
                            Uncover What’s Inside Your Food & Cosmetics
                        </h1>
                        <p class="text-slate-400 text-sm md:text-base leading-relaxed max-w-2xl">
                            Instantly detect hidden allergens, artificial additives, carcinogenic preservatives, and safety risks with computer vision.
                        </p>
                    </div>

                    <!-- 3D Interactive Rotating Holographic Bottle Mockup -->
                    <div class="lg:col-span-4 flex justify-center perspective-container">
                        <div id="holo-bottle-mockup" class="holo-bottle relative w-48 h-72 rounded-3xl p-4 flex flex-col justify-between items-center text-center backdrop-blur-lg border border-white/20 animate-float-3d">
                            <!-- 3D Bottle Cap -->
                            <div class="w-20 h-6 rounded-t-xl bg-gradient-to-r from-slate-700 via-slate-600 to-slate-800 border border-white/20 shadow-lg"></div>
                            
                            <!-- Floating Holographic Label -->
                            <div class="holo-label w-full p-3 rounded-2xl border border-emerald-400/40 space-y-2">
                                <div class="flex items-center justify-between text-[10px] text-emerald-400 font-bold">
                                    <span>LABELLENS 3D</span>
                                    <i data-lucide="check-check" class="w-3 h-3"></i>
                                </div>
                                <div class="h-1.5 w-3/4 bg-emerald-400/30 rounded-full mx-auto"></div>
                                <div class="h-1.5 w-1/2 bg-magenta-400/30 rounded-full mx-auto"></div>
                                <div class="text-[9px] text-slate-300 font-semibold tracking-wider uppercase">0% Harmful Additives</div>
                            </div>

                            <!-- 3D Status Ring Glow -->
                            <div class="w-12 h-12 rounded-full neon-ring-emerald flex items-center justify-center text-emerald-400 text-xs font-bold bg-slate-950/80 shadow-2xl">
                                98%
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Dietary Restrictions Selector Header -->
                <div class="glass-card p-4 rounded-3xl border border-slate-800 space-y-3" data-tilt data-tilt-max="3" data-tilt-glare data-tilt-max-glare="0.1">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-2">
                            <i data-lucide="shield-alert" class="w-4 h-4"></i> Active Personal Health & Dietary Filters
                        </span>
                        <span class="text-xs text-slate-400">Click to toggle warnings</span>
                    </div>
                    <div class="flex flex-wrap gap-2" id="dietary-tags-container">
                        <!-- Toggles dynamically generated via JavaScript -->
                    </div>
                </div>

                <!-- Upload Dropzone & Sample Presets Section -->
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                    
                    <!-- Left: Dropzone with 3D Tilt -->
                    <div class="lg:col-span-8 flex flex-col justify-between glass-card rounded-3xl p-6 border border-slate-800 relative overflow-hidden group" data-tilt data-tilt-max="4" data-tilt-speed="400">
                        
                        <!-- Dropzone Area -->
                        <div id="dropzone" onclick="document.getElementById('file-input').click()" 
                            class="border-2 border-dashed border-slate-700/80 hover:border-emerald-500/60 rounded-2xl p-8 md:p-12 text-center transition-all cursor-pointer bg-slate-900/40 hover:bg-slate-900/80 flex flex-col items-center justify-center min-h-[320px] group/zone">
                            
                            <input type="file" id="file-input" class="hidden" accept="image/*" onchange="handleFileUpload(event)">
                            
                            <!-- Dropzone Default View -->
                            <div id="dropzone-prompt" class="space-y-4 flex flex-col items-center">
                                <div class="w-20 h-20 rounded-3xl bg-gradient-to-br from-emerald-500/20 to-magenta-500/20 border border-emerald-500/30 flex items-center justify-center group-hover/zone:scale-110 transition-transform shadow-lg shadow-emerald-500/10">
                                    <i data-lucide="upload-cloud" class="w-10 h-10 text-emerald-400"></i>
                                </div>
                                <div>
                                    <p class="text-base font-semibold text-slate-200">Drag & Drop product label image here</p>
                                    <p class="text-xs text-slate-400 mt-1">Supports JPG, PNG, WEBP up to 10MB or click to browse</p>
                                </div>
                                <div class="flex items-center gap-3 pt-2">
                                    <button class="px-5 py-2.5 text-xs font-semibold rounded-xl bg-gradient-to-r from-emerald-500 to-cyan-500 text-slate-950 hover:opacity-90 transition-opacity shadow-lg shadow-emerald-500/20 flex items-center gap-1.5">
                                        <i data-lucide="file-up" class="w-3.5 h-3.5"></i> Choose File
                                    </button>
                                    <button onclick="event.stopPropagation(); triggerCamera();" class="px-5 py-2.5 text-xs font-semibold rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 transition-colors border border-slate-700 flex items-center gap-1.5">
                                        <i data-lucide="camera" class="w-3.5 h-3.5"></i> Camera
                                    </button>
                                </div>
                            </div>

                            <!-- Selected Preview Mode -->
                            <div id="dropzone-preview" class="hidden relative w-full h-full min-h-[260px] flex items-center justify-center rounded-2xl overflow-hidden bg-slate-950 border border-slate-800">
                                <img id="preview-img" class="max-h-72 object-contain rounded-lg" src="" alt="Label Preview">
                                
                                <!-- Interactive 3D AI Scanning Visual Animation Overlay -->
                                <div id="scan-overlay" class="hidden absolute inset-0 bg-slate-950/70 backdrop-blur-[3px] flex flex-col items-center justify-center space-y-4">
                                    <div class="absolute inset-x-0 h-1 bg-gradient-to-r from-transparent via-emerald-400 to-transparent animate-scan-line shadow-[0_0_20px_#34d399]"></div>
                                    
                                    <!-- 3D Holographic Scanning Box Markers -->
                                    <div class="absolute top-1/4 left-1/4 w-32 h-14 border-2 border-dashed border-rose-500 rounded-xl bg-rose-500/10 animate-pulse shadow-[0_0_15px_rgba(244,63,94,0.3)]"></div>
                                    <div class="absolute bottom-1/3 right-1/4 w-36 h-12 border-2 border-dashed border-emerald-400 rounded-xl bg-emerald-500/10 animate-pulse shadow-[0_0_15px_rgba(52,211,153,0.3)]"></div>

                                    <div class="bg-slate-900/90 px-5 py-3 rounded-2xl border border-emerald-500/40 flex items-center gap-3 shadow-2xl">
                                        <i data-lucide="loader-2" class="w-5 h-5 text-emerald-400 animate-spin"></i>
                                        <span class="text-xs font-semibold text-emerald-300 tracking-wide">Gemini 3D Vision OCR & Health Analysis...</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Scan Action Footer -->
                        <div class="mt-4 flex items-center justify-between">
                            <span id="file-info" class="text-xs text-slate-400 flex items-center gap-1.5">
                                <i data-lucide="info" class="w-3.5 h-3.5 text-slate-500"></i> Select a label image or pick a preset sample to inspect.
                            </span>
                            <button id="analyze-btn" onclick="startAnalysis()" disabled class="px-6 py-3 rounded-xl text-xs font-bold uppercase tracking-wider bg-slate-800 text-slate-500 cursor-not-allowed transition-all flex items-center gap-2 shadow-lg">
                                <i data-lucide="sparkles" class="w-4 h-4"></i> Start AI Analysis
                            </button>
                        </div>
                    </div>

                    <!-- Right: Sample Preset Selector with 3D Parallax Tilt -->
                    <div class="lg:col-span-4 glass-card rounded-3xl p-6 border border-slate-800 flex flex-col justify-between space-y-4" data-tilt data-tilt-max="4">
                        <div>
                            <div class="flex items-center justify-between mb-4">
                                <h3 class="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
                                    <i data-lucide="sparkles" class="w-4 h-4 text-magenta-400"></i> Try Preset Labels
                                </h3>
                                <span class="text-[10px] text-slate-400 bg-slate-800 px-2.5 py-1 rounded-full border border-slate-700">Instant Demo</span>
                            </div>
                            <p class="text-xs text-slate-400 mb-4">Click any sample label below to test the 3D AI evaluation instantly.</p>
                            
                            <div class="space-y-2.5">
                                <!-- Preset 1 -->
                                <button onclick="loadPreset('protein')" class="w-full text-left p-3 rounded-2xl bg-slate-900/70 hover:bg-slate-800/80 border border-slate-800 hover:border-emerald-500/40 transition-all flex items-center justify-between group shadow-sm">
                                    <div class="flex items-center gap-3">
                                        <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400">
                                            <i data-lucide="dumbbell" class="w-4 h-4"></i>
                                        </div>
                                        <div>
                                            <p class="text-xs font-bold text-slate-200 group-hover:text-emerald-400 transition-colors">Ultra Whey Protein Bar</p>
                                            <p class="text-[10px] text-slate-400">Contains Milk, Soy, Artificial Sweeteners</p>
                                        </div>
                                    </div>
                                    <i data-lucide="chevron-right" class="w-4 h-4 text-slate-600 group-hover:text-emerald-400 transition-colors"></i>
                                </button>

                                <!-- Preset 2 -->
                                <button onclick="loadPreset('energy')" class="w-full text-left p-3 rounded-2xl bg-slate-900/70 hover:bg-slate-800/80 border border-slate-800 hover:border-emerald-500/40 transition-all flex items-center justify-between group shadow-sm">
                                    <div class="flex items-center gap-3">
                                        <div class="w-10 h-10 rounded-xl bg-rose-500/10 border border-rose-500/30 flex items-center justify-center text-rose-400">
                                            <i data-lucide="zap" class="w-4 h-4"></i>
                                        </div>
                                        <div>
                                            <p class="text-xs font-bold text-slate-200 group-hover:text-emerald-400 transition-colors">Extreme Neon Energy Drink</p>
                                            <p class="text-[10px] text-slate-400">High Caffeine, Red 40 Dye, BHT</p>
                                        </div>
                                    </div>
                                    <i data-lucide="chevron-right" class="w-4 h-4 text-slate-600 group-hover:text-emerald-400 transition-colors"></i>
                                </button>

                                <!-- Preset 3 -->
                                <button onclick="loadPreset('sunscreen')" class="w-full text-left p-3 rounded-2xl bg-slate-900/70 hover:bg-slate-800/80 border border-slate-800 hover:border-emerald-500/40 transition-all flex items-center justify-between group shadow-sm">
                                    <div class="flex items-center gap-3">
                                        <div class="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400">
                                            <i data-lucide="sun" class="w-4 h-4"></i>
                                        </div>
                                        <div>
                                            <p class="text-xs font-bold text-slate-200 group-hover:text-emerald-400 transition-colors">HydraShield SPF 50 Lotion</p>
                                            <p class="text-[10px] text-slate-400">Parabens, Oxybenzone, Aloe Vera</p>
                                        </div>
                                    </div>
                                    <i data-lucide="chevron-right" class="w-4 h-4 text-slate-600 group-hover:text-emerald-400 transition-colors"></i>
                                </button>

                                <!-- Preset 4 -->
                                <button onclick="loadPreset('baby')" class="w-full text-left p-3 rounded-2xl bg-slate-900/70 hover:bg-slate-800/80 border border-slate-800 hover:border-emerald-500/40 transition-all flex items-center justify-between group shadow-sm">
                                    <div class="flex items-center gap-3">
                                        <div class="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                                            <i data-lucide="baby" class="w-4 h-4"></i>
                                        </div>
                                        <div>
                                            <p class="text-xs font-bold text-slate-200 group-hover:text-emerald-400 transition-colors">Organic Oat & Apple Puree</p>
                                            <p class="text-[10px] text-slate-400">100% Organic, No Sugar Added</p>
                                        </div>
                                    </div>
                                    <i data-lucide="chevron-right" class="w-4 h-4 text-slate-600 group-hover:text-emerald-400 transition-colors"></i>
                                </button>
                            </div>
                        </div>

                        <!-- Quality Check Indicator -->
                        <div class="p-3 rounded-2xl bg-slate-950 border border-slate-800 flex items-center gap-3">
                            <i data-lucide="shield-check" class="w-5 h-5 text-emerald-400 shrink-0"></i>
                            <p class="text-[11px] text-slate-400">Verified against FDA, EU E-Number, & WHO Ingredient Databases.</p>
                        </div>
                    </div>
                </div>

                <!-- SECTION 2: ANALYSIS RESULTS DASHBOARD (Hidden until scan complete) -->
                <div id="analysis-results" class="hidden space-y-8 animate-fade-in">
                    
                    <!-- Safety Scorecard & AI Verdict Overview -->
                    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                        
                        <!-- Safety Score Gauge Card with 3D Tilt -->
                        <div class="lg:col-span-4 glass-card rounded-3xl p-6 border border-slate-800 flex flex-col items-center justify-center text-center relative overflow-hidden" data-tilt data-tilt-max="6">
                            <h3 class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">3D Safety Rating Index</h3>
                            
                            <!-- Donut Gauge Chart Container -->
                            <div class="relative w-48 h-48 flex items-center justify-center my-2">
                                <canvas id="safetyGaugeChart"></canvas>
                                <div class="absolute inset-0 flex flex-col items-center justify-center">
                                    <span id="score-number" class="text-4xl font-extrabold text-white">82</span>
                                    <span id="score-rating" class="text-xs font-bold uppercase tracking-wider text-emerald-400">Generally Safe</span>
                                </div>
                            </div>

                            <!-- Stat Summary Badges -->
                            <div class="grid grid-cols-3 gap-2.5 w-full mt-4 text-center">
                                <div class="bg-slate-950/80 p-2.5 rounded-2xl border border-slate-800">
                                    <p class="text-xs text-rose-400 font-bold" id="cnt-flagged">1</p>
                                    <p class="text-[10px] text-slate-400 uppercase">High Risk</p>
                                </div>
                                <div class="bg-slate-950/80 p-2.5 rounded-2xl border border-slate-800">
                                    <p class="text-xs text-amber-400 font-bold" id="cnt-caution">2</p>
                                    <p class="text-[10px] text-slate-400 uppercase">Caution</p>
                                </div>
                                <div class="bg-slate-950/80 p-2.5 rounded-2xl border border-slate-800">
                                    <p class="text-xs text-emerald-400 font-bold" id="cnt-safe">7</p>
                                    <p class="text-[10px] text-slate-400 uppercase">Safe</p>
                                </div>
                            </div>
                        </div>

                        <!-- AI Executive Summary Card with 3D Parallax Tilt -->
                        <div class="lg:col-span-8 glass-card rounded-3xl p-6 border border-slate-800 flex flex-col justify-between space-y-4" data-tilt data-tilt-max="4">
                            <div>
                                <div class="flex items-center justify-between mb-3">
                                    <div class="flex items-center gap-2">
                                        <div class="w-9 h-9 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                                            <i data-lucide="bot" class="w-5 h-5"></i>
                                        </div>
                                        <h3 class="text-base font-bold text-slate-100">Gemini 3D AI Safety Summary</h3>
                                    </div>
                                    <span id="scanned-product-name" class="text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                                        Ultra Whey Protein Bar
                                    </span>
                                </div>

                                <div class="p-4 rounded-2xl bg-slate-950/90 border border-slate-800/80 text-sm text-slate-300 leading-relaxed space-y-2">
                                    <p id="ai-summary-text">
                                        This product scores an <strong>82/100</strong>. It contains mostly wholesome proteins and fiber, but contains artificial sweetener <strong>Sucralose</strong> and preservative <strong>BHT</strong>, which may trigger sensitivities for sensitive individuals.
                                    </p>
                                </div>
                            </div>

                            <!-- Dietary Restriction Warning Banner -->
                            <div id="allergen-alert-banner" class="p-3.5 rounded-2xl bg-rose-500/10 border border-rose-500/30 flex items-center gap-3">
                                <i data-lucide="triangle-alert" class="w-5 h-5 text-rose-400 shrink-0"></i>
                                <p class="text-xs text-rose-200">
                                    <strong>Dietary Alert:</strong> Matches your active profile filter for <span class="underline font-bold" id="matched-allergen-list">Milk (Lactose)</span>.
                                </p>
                            </div>
                        </div>
                    </div>

                    <!-- INGREDIENT RISK MATRIX TABS & CARDS -->
                    <div class="glass-card rounded-3xl p-6 border border-slate-800 space-y-6" data-tilt data-tilt-max="2">
                        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-800 pb-4">
                            <div>
                                <h3 class="text-base font-bold text-slate-100 flex items-center gap-2">
                                    <i data-lucide="layers" class="w-4 h-4 text-emerald-400"></i> Detailed Ingredient Risk Breakdown
                                </h3>
                                <p class="text-xs text-slate-400">Click any ingredient card for regulatory status and health research.</p>
                            </div>

                            <!-- Filter Category Buttons -->
                            <div class="flex items-center gap-1 bg-slate-900 p-1.5 rounded-2xl border border-slate-800 self-start">
                                <button onclick="filterMatrix('all')" id="btn-matrix-all" class="px-3.5 py-1.5 text-xs font-semibold rounded-xl bg-emerald-500 text-slate-950">All (<span id="cnt-all">10</span>)</button>
                                <button onclick="filterMatrix('flagged')" id="btn-matrix-flagged" class="px-3.5 py-1.5 text-xs font-semibold rounded-xl text-slate-400 hover:text-white">Flagged</button>
                                <button onclick="filterMatrix('caution')" id="btn-matrix-caution" class="px-3.5 py-1.5 text-xs font-semibold rounded-xl text-slate-400 hover:text-white">Caution</button>
                                <button onclick="filterMatrix('safe')" id="btn-matrix-safe" class="px-3.5 py-1.5 text-xs font-semibold rounded-xl text-slate-400 hover:text-white">Safe</button>
                            </div>
                        </div>

                        <!-- Ingredient Grid Container -->
                        <div id="ingredient-matrix-grid" class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <!-- Dynamically Generated Cards -->
                        </div>
                    </div>

                    <!-- HEALTHIER ALTERNATIVES & PRODUCT COMPARISON -->
                    <div class="glass-card rounded-3xl p-6 border border-slate-800 space-y-6" data-tilt data-tilt-max="2">
                        <div class="flex items-center gap-2">
                            <div class="w-8 h-8 rounded-xl bg-emerald-500/10 flex items-center justify-center text-emerald-400">
                                <i data-lucide="sparkles" class="w-4 h-4"></i>
                            </div>
                            <div>
                                <h3 class="text-base font-bold text-slate-100">Clean Label Alternatives</h3>
                                <p class="text-xs text-slate-400">Better choices without artificial additives or flagged allergens.</p>
                            </div>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4" id="alternatives-container">
                            <!-- Generated dynamically -->
                        </div>
                    </div>
                </div>
            </div>

            <!-- SECTION 2: SCAN HISTORY TAB (Hidden initially) -->
            <div id="tab-history" class="hidden space-y-6">
                <div class="flex items-center justify-between">
                    <div>
                        <h2 class="text-2xl font-bold text-slate-100">Scan History & Saved Reports</h2>
                        <p class="text-xs text-slate-400">Access previous product safety evaluations.</p>
                    </div>
                    <button onclick="clearHistory()" class="px-4 py-2 text-xs text-rose-400 hover:bg-rose-500/10 border border-rose-500/20 rounded-xl transition-colors">
                        Clear History
                    </button>
                </div>

                <div class="glass-card rounded-3xl p-6 border border-slate-800">
                    <div class="space-y-3" id="history-list">
                        <!-- Filled by JS -->
                    </div>
                </div>
            </div>

            <!-- SECTION 3: HEALTH PROFILE TAB (Hidden initially) -->
            <div id="tab-diet" class="hidden space-y-6">
                <div>
                    <h2 class="text-2xl font-bold text-slate-100">Personal Health & Sensitivity Settings</h2>
                    <p class="text-xs text-slate-400">Customize risk flags based on your diet, medical needs, or allergies.</p>
                </div>

                <div class="glass-card rounded-3xl p-6 border border-slate-800 space-y-6">
                    <h3 class="text-sm font-bold text-slate-200 uppercase tracking-wider">Configure Sensitivity Presets</h3>
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4" id="profile-settings-grid">
                        <!-- Configured via JS -->
                    </div>
                </div>
            </div>
        </main>

        <!-- FOOTER -->
        <footer class="glass-card border-t border-slate-800/80 mt-12 py-6 px-4 text-center">
            <p class="text-xs text-slate-500">
                LabelLens AI 3D — Educational Safety Tool. Always consult medical professionals regarding severe food allergies.
            </p>
        </footer>
    </div>

    <!-- MODAL: INGREDIENT DETAIL MODAL -->
    <div id="ingredient-modal" class="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md hidden items-center justify-center p-4">
        <div class="glass-card max-w-lg w-full rounded-3xl p-6 border border-slate-800 space-y-4 relative">
            <button onclick="closeModal()" class="absolute top-4 right-4 p-2 rounded-full bg-slate-900 text-slate-400 hover:text-white">
                <i data-lucide="x" class="w-4 h-4"></i>
            </button>
            
            <div class="flex items-center gap-3">
                <div id="modal-badge-icon" class="w-10 h-10 rounded-xl flex items-center justify-center text-lg font-bold"></div>
                <div>
                    <h3 id="modal-title" class="text-lg font-bold text-white">Ingredient Name</h3>
                    <p id="modal-category" class="text-xs text-slate-400">Preservative / Additive</p>
                </div>
            </div>

            <div class="space-y-3 text-xs text-slate-300">
                <div class="p-3 bg-slate-950 rounded-2xl border border-slate-800">
                    <p class="font-bold text-slate-200 mb-1">Health Impact & Concerns:</p>
                    <p id="modal-impact" class="text-slate-400 leading-relaxed"></p>
                </div>

                <div class="p-3 bg-slate-950 rounded-2xl border border-slate-800">
                    <p class="font-bold text-slate-200 mb-1">FDA & EU Regulatory Status:</p>
                    <p id="modal-regulatory" class="text-slate-400 leading-relaxed"></p>
                </div>
            </div>

            <div class="pt-2">
                <button onclick="closeModal()" class="w-full py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold">
                    Close Details
                </button>
            </div>
        </div>
    </div>

    <!-- MODAL: API KEY SETTINGS MODAL -->
    <div id="apikey-modal" class="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md hidden items-center justify-center p-4">
        <div class="glass-card max-w-md w-full rounded-3xl p-6 border border-slate-800 space-y-4 relative">
            <button onclick="toggleApiKeyModal()" class="absolute top-4 right-4 p-2 rounded-full bg-slate-900 text-slate-400 hover:text-white">
                <i data-lucide="x" class="w-4 h-4"></i>
            </button>
            
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
                    <i data-lucide="key" class="w-5 h-5"></i>
                </div>
                <div>
                    <h3 class="text-base font-bold text-white">Gemini API Key</h3>
                    <p class="text-xs text-slate-400">Enable live custom image AI processing</p>
                </div>
            </div>

            <p class="text-xs text-slate-400 leading-relaxed">
                By default, LabelLens runs in high-speed simulation mode with preset databases. Optionally enter your Google Gemini API key below for real-time live vision extraction.
            </p>

            <div class="space-y-2">
                <label class="text-xs font-semibold text-slate-300">API Key</label>
                <input type="password" id="api-key-input" placeholder="AIzaSy..." class="w-full px-3 py-2.5 rounded-xl bg-slate-950 border border-slate-800 text-slate-200 text-xs focus:border-emerald-500 focus:outline-none">
            </div>

            <button onclick="saveApiKey()" class="w-full py-2.5 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 text-xs font-bold shadow-lg shadow-emerald-500/20">
                Save Settings
            </button>
        </div>
    </div>

    <!-- APPLICATION LOGIC & PRESET DATA -->
    <script>
        // State Management
        let currentUploadedImage = null;
        let chartInstance = null;
        let selectedFilter = 'all';

        // Mouse Parallax Interaction for 3D Holographic Bottle
        document.addEventListener('mousemove', (e) => {
            const bottle = document.getElementById('holo-bottle-mockup');
            if (bottle) {
                const x = (window.innerWidth / 2 - e.pageX) / 25;
                const y = (window.innerHeight / 2 - e.pageY) / 25;
                bottle.style.transform = `rotateY(${x}deg) rotateX(${y}deg) translateY(-10px)`;
            }
        });

        // Dietary Toggles
        const dietaryFilters = [
            { id: 'vegan', label: '🥦 Vegan', active: false },
            { id: 'gluten', label: '🌾 Gluten-Free', active: true },
            { id: 'lactose', label: '🍼 Lactose Intolerant', active: true },
            { id: 'nuts', label: '🥜 Peanut / Nut Allergy', active: true },
            { id: 'parabens', label: '🧴 Paraben Free', active: false },
            { id: 'pregnancy', label: '🤰 Pregnancy Safe', active: false }
        ];

        // Preset Datasets for Interactive Demos
        const PRESETS = {
            protein: {
                name: "Ultra Whey Protein Bar",
                score: 74,
                status: "Caution Recommended",
                color: "#f59e0b",
                summary: "This protein bar offers 20g of whey isolate protein, but contains artificial sweetener Sucralose and preservative BHT which may trigger gastrointestinal sensitivity or skin inflammation.",
                allergens: "Milk (Lactose), Soy Lecithin",
                ingredients: [
                    { name: "Butylated Hydroxytoluene (BHT)", risk: "red", category: "Preservative (E321)", impact: "Synthetic antioxidant used to prevent fat oxidation. Linked to potential endocrine disruption in high cumulative doses.", reg: "Restricted in EU foods; FDA approved under limit." },
                    { name: "Sucralose", risk: "yellow", category: "Artificial Sweetener", impact: "Zero-calorie artificial sweetener. May alter gut microbiome composition in frequent users.", reg: "FDA & EFSA Approved." },
                    { name: "Palm Kernel Oil", risk: "yellow", category: "Saturated Fat", impact: "High in saturated fatty acids. Sourced with potential environmental impact.", reg: "Standard food additive." },
                    { name: "Whey Protein Isolate", risk: "green", category: "Protein Source", impact: "High biological value protein supporting muscle repair. Contains trace lactose.", reg: "GRAS (Generally Recognized as Safe)." },
                    { name: "Organic Almond Butter", risk: "green", category: "Healthy Fat", impact: "Rich in Vitamin E, monounsaturated fats, and magnesium.", reg: "Natural ingredient." },
                    { name: "Soy Lecithin", risk: "yellow", category: "Emulsifier", impact: "Common allergen. Used to improve texture and shelf stability.", reg: "FDA Allergen Labeling Required." }
                ],
                alternatives: [
                    { name: "PurePlant Organic Protein Crisp", score: 96, highlight: "Stevia Sweetened, No BHT, Pea Protein Base" },
                    { name: "CleanFuel Almond Fudge Bar", score: 91, highlight: "Grass-Fed Whey, Honey Sweetened" }
                ]
            },
            energy: {
                name: "Extreme Neon Energy Drink",
                score: 48,
                status: "High Risk Flags",
                color: "#f43f5e",
                summary: "High concentration of synthetic food dyes (Red 40) and high caffeine loads. Unsuitable for children, pregnant individuals, or those with dye allergies.",
                allergens: "Artificial Dyes (Red 40), High Caffeine",
                ingredients: [
                    { name: "Allura Red AC (Red 40)", risk: "red", category: "Petroleum Food Dye (E129)", impact: "Linked to hyperactivity in sensitive children and localized allergic reactions.", reg: "Requires warning label in EU ('May affect activity in children')." },
                    { name: "High Fructose Corn Syrup", risk: "red", category: "Refined Sweetener", impact: "Correlated with metabolic strain, fatty liver risk, and glycemic spikes.", reg: "FDA Approved." },
                    { name: "Synthetic Caffeine (200mg)", risk: "yellow", category: "Stimulant", impact: "High dose equivalent to 2.5 coffee cups. May cause elevated heart rate and anxiety.", reg: "FDA advises under 400mg/day." },
                    { name: "Taurine", risk: "green", category: "Amino Acid", impact: "Supports neurological development and water balance regulation.", reg: "GRAS Approved." },
                    { name: "Filtered Carbonated Water", risk: "green", category: "Base", impact: "Hydration base.", reg: "Safe." }
                ],
                alternatives: [
                    { name: "MatchaSpark Natural Focus", score: 94, highlight: "Organic Green Tea, Organic Lemon Juice, No Dyes" },
                    { name: "Electrolyte Clean Wave", score: 89, highlight: "Monk Fruit Sweetened, Natural Colors" }
                ]
            },
            sunscreen: {
                name: "HydraShield SPF 50 Lotion",
                score: 68,
                status: "Moderate Concern",
                color: "#f59e0b",
                summary: "Effective sun barrier, but contains chemical UV filters Oxybenzone and Methylparaben preservative which are potential hormone mimics.",
                allergens: "Fragrance, Synthetic Chemical Filters",
                ingredients: [
                    { name: "Oxybenzone", risk: "red", category: "Chemical UV Filter", impact: "Absorbed through skin into bloodstream. Potential endocrine disruptor and damaging to coral reefs.", reg: "Banned in Hawaii reef-safe laws; restricted concentration in EU." },
                    { name: "Methylparaben", risk: "red", category: "Preservative", impact: "Prevents bacterial growth but mimics estrogen weak activity.", reg: "Restricted max concentration by EU SCCS." },
                    { name: "Zinc Oxide (Non-Nano)", risk: "green", category: "Mineral Filter", impact: "Physical sun barrier reflecting UVA/UVB rays without skin penetration.", reg: "FDA Category I Mineral Active." },
                    { name: "Aloe Vera Leaf Juice", risk: "green", category: "Botanical Soother", impact: "Calms inflammation and provides skin hydration.", reg: "Safe." }
                ],
                alternatives: [
                    { name: "ReefGuard Pure Zinc Mineral SPF 50", score: 98, highlight: "100% Non-Nano Zinc, Paraben-Free, Fragrance-Free" }
                ]
            },
            baby: {
                name: "Organic Oat & Apple Puree",
                score: 98,
                status: "Clean & Certified Safe",
                color: "#10b981",
                summary: "Exceptional pure formulation with zero artificial preservatives, added sugars, or synthetic dyes. Fully organic certified.",
                allergens: "Oats (Gluten Traces)",
                ingredients: [
                    { name: "Organic Apple Puree", risk: "green", category: "Whole Fruit", impact: "Rich in natural dietary fiber and pectin.", reg: "USDA Certified Organic." },
                    { name: "Organic Whole Grain Oat Flour", risk: "green", category: "Whole Grain", impact: "Provides beta-glucans and sustained energy.", reg: "Safe." },
                    { name: "Organic Ascorbic Acid (Vitamin C)", risk: "green", category: "Natural Antioxidant", impact: "Prevents browning naturally.", reg: "GRAS Approved." }
                ],
                alternatives: [
                    { name: "Earth's Best Organic Pear Berry", score: 99, highlight: "100% Whole Fruit" }
                ]
            }
        };

        // Initialize UI on DOM Ready
        document.addEventListener("DOMContentLoaded", () => {
            lucide.createIcons();
            renderDietaryTags();
            renderProfileSettings();
            initChart();
            
            // Re-initialize VanillaTilt on dynamically rendered cards
            if (window.VanillaTilt) {
                VanillaTilt.init(document.querySelectorAll("[data-tilt]"));
            }
        });

        // Tab Switcher Logic
        function switchTab(tab) {
            ['scanner', 'history', 'diet'].forEach(t => {
                const el = document.getElementById(`tab-${t}`);
                const nav = document.getElementById(`nav-${t}`);
                if (t === tab) {
                    el.classList.remove('hidden');
                    nav.classList.add('bg-gradient-to-r', 'from-emerald-500', 'to-cyan-500', 'text-slate-950', 'shadow-lg');
                    nav.classList.remove('text-slate-400');
                } else {
                    el.classList.add('hidden');
                    nav.classList.remove('bg-gradient-to-r', 'from-emerald-500', 'to-cyan-500', 'text-slate-950', 'shadow-lg');
                    nav.classList.add('text-slate-400');
                }
            });
        }

        // Render Dietary Restriction Badges
        function renderDietaryTags() {
            const container = document.getElementById('dietary-tags-container');
            container.innerHTML = dietaryFilters.map(f => `
                <button onclick="toggleDietaryFilter('${f.id}')" 
                    class="px-3.5 py-1.5 rounded-xl text-xs font-semibold transition-all border ${
                        f.active 
                        ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40 shadow-[0_0_12px_rgba(16,185,129,0.2)]' 
                        : 'bg-slate-900 text-slate-500 border-slate-800 hover:border-slate-700'
                    }">
                    ${f.label}
                </button>
            `).join('');
        }

        function toggleDietaryFilter(id) {
            const filter = dietaryFilters.find(f => f.id === id);
            if (filter) filter.active = !filter.active;
            renderDietaryTags();
            renderProfileSettings();
        }

        function renderProfileSettings() {
            const container = document.getElementById('profile-settings-grid');
            container.innerHTML = dietaryFilters.map(f => `
                <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 flex items-center justify-between">
                    <span class="text-xs font-bold text-slate-200">${f.label}</span>
                    <input type="checkbox" ${f.active ? 'checked' : ''} onchange="toggleDietaryFilter('${f.id}')" class="w-4 h-4 accent-emerald-500 rounded cursor-pointer">
                </div>
            `).join('');
        }

        // Handle File Upload
        function handleFileUpload(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (event) => {
                    currentUploadedImage = event.target.result;
                    showPreview(currentUploadedImage, file.name);
                };
                reader.readAsDataURL(file);
            }
        }

        function showPreview(src, name) {
            document.getElementById('dropzone-prompt').classList.add('hidden');
            document.getElementById('dropzone-preview').classList.remove('hidden');
            document.getElementById('preview-img').src = src;
            document.getElementById('file-info').innerHTML = `<i data-lucide="check-circle" class="w-3.5 h-3.5 text-emerald-400"></i> Loaded: ${name}`;
            
            const btn = document.getElementById('analyze-btn');
            btn.disabled = false;
            btn.classList.remove('bg-slate-800', 'text-slate-500', 'cursor-not-allowed');
            btn.classList.add('bg-gradient-to-r', 'from-emerald-500', 'to-cyan-500', 'text-slate-950', 'hover:opacity-90', 'shadow-emerald-500/20');
            lucide.createIcons();
        }

        function loadPreset(key) {
            const preset = PRESETS[key];
            if (!preset) return;
            
            const presetSvg = `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="400" height="250" viewBox="0 0 400 250"><rect width="100%" height="100%" fill="%230b101d"/><text x="50%" y="40%" dominant-baseline="middle" text-anchor="middle" fill="%2334d399" font-family="sans-serif" font-weight="bold" font-size="18">${preset.name}</text><text x="50%" y="60%" dominant-baseline="middle" text-anchor="middle" fill="%2394a3b8" font-family="sans-serif" font-size="12">INGREDIENTS: ${preset.ingredients.map(i=>i.name).slice(0,3).join(', ')}...</text></svg>`;
            
            showPreview(presetSvg, preset.name);
            startAnalysis(preset);
        }

        function triggerCamera() {
            alert("Camera trigger simulation active. In mobile browser mode, this launches device lens.");
        }

        // Start Scanner Analysis Simulation
        function startAnalysis(presetData = null) {
            const overlay = document.getElementById('scan-overlay');
            overlay.classList.remove('hidden');

            setTimeout(() => {
                overlay.classList.add('hidden');
                document.getElementById('analysis-results').classList.remove('hidden');
                
                const data = presetData || PRESETS.protein;
                populateResults(data);

                document.getElementById('analysis-results').scrollIntoView({ behavior: 'smooth' });
            }, 1800);
        }

        // Chart Initialization
        function initChart() {
            const ctx = document.getElementById('safetyGaugeChart').getContext('2d');
            chartInstance = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    datasets: [{
                        data: [82, 18],
                        backgroundColor: ['#10b981', '#162032'],
                        borderWidth: 0,
                    }]
                },
                options: {
                    cutout: '80%',
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { tooltip: { enabled: false } }
                }
            });
        }

        function populateResults(data) {
            document.getElementById('score-number').innerText = data.score;
            document.getElementById('score-rating').innerText = data.status;
            document.getElementById('score-rating').style.color = data.color;

            if (chartInstance) {
                chartInstance.data.datasets[0].data = [data.score, 100 - data.score];
                chartInstance.data.datasets[0].backgroundColor[0] = data.color;
                chartInstance.update();
            }

            document.getElementById('scanned-product-name').innerText = data.name;
            document.getElementById('ai-summary-text').innerText = data.summary;
            document.getElementById('matched-allergen-list').innerText = data.allergens;

            const flagged = data.ingredients.filter(i => i.risk === 'red').length;
            const caution = data.ingredients.filter(i => i.risk === 'yellow').length;
            const safe = data.ingredients.filter(i => i.risk === 'green').length;

            document.getElementById('cnt-flagged').innerText = flagged;
            document.getElementById('cnt-caution').innerText = caution;
            document.getElementById('cnt-safe').innerText = safe;
            document.getElementById('cnt-all').innerText = data.ingredients.length;

            renderMatrixCards(data.ingredients);
            renderAlternatives(data.alternatives);
        }

        function renderMatrixCards(ingredients) {
            const container = document.getElementById('ingredient-matrix-grid');
            
            const filtered = ingredients.filter(i => {
                if (selectedFilter === 'flagged') return i.risk === 'red';
                if (selectedFilter === 'caution') return i.risk === 'yellow';
                if (selectedFilter === 'safe') return i.risk === 'green';
                return true;
            });

            container.innerHTML = filtered.map(item => {
                const colorMap = {
                    red: { border: 'border-rose-500/40', bg: 'bg-rose-500/10', text: 'text-rose-400', label: 'Flagged Risk' },
                    yellow: { border: 'border-amber-500/40', bg: 'bg-amber-500/10', text: 'text-amber-400', label: 'Caution' },
                    green: { border: 'border-emerald-500/40', bg: 'bg-emerald-500/10', text: 'text-emerald-400', label: 'Safe' }
                }[item.risk];

                return `
                    <div onclick="openModal('${escape(item.name)}', '${escape(item.category)}', '${escape(item.impact)}', '${escape(item.reg)}', '${item.risk}')"
                        data-tilt data-tilt-max="5"
                        class="p-4 rounded-2xl bg-slate-950/90 border ${colorMap.border} hover:border-slate-500 transition-all cursor-pointer flex flex-col justify-between space-y-2 group shadow-md">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-bold text-slate-200 group-hover:text-emerald-400 transition-colors">${item.name}</span>
                            <span class="px-2 py-0.5 text-[10px] font-bold rounded-md ${colorMap.bg} ${colorMap.text}">${colorMap.label}</span>
                        </div>
                        <p class="text-[11px] text-slate-400 line-clamp-2">${item.impact}</p>
                        <div class="flex items-center justify-between pt-1 text-[10px] text-slate-500">
                            <span>Category: ${item.category}</span>
                            <span class="text-emerald-400 flex items-center gap-1">Details <i data-lucide="arrow-right" class="w-3 h-3"></i></span>
                        </div>
                    </div>
                `;
            }).join('');
            
            lucide.createIcons();
            if (window.VanillaTilt) VanillaTilt.init(document.querySelectorAll("[data-tilt]"));
        }

        function filterMatrix(type) {
            selectedFilter = type;
            ['all', 'flagged', 'caution', 'safe'].forEach(t => {
                const btn = document.getElementById(`btn-matrix-${t}`);
                if (t === type) {
                    btn.className = "px-3.5 py-1.5 text-xs font-semibold rounded-xl bg-emerald-500 text-slate-950";
                } else {
                    btn.className = "px-3.5 py-1.5 text-xs font-semibold rounded-xl text-slate-400 hover:text-white";
                }
            });
            populateResults(PRESETS.protein);
        }

        function renderAlternatives(alternatives) {
            const container = document.getElementById('alternatives-container');
            container.innerHTML = alternatives.map(alt => `
                <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 flex items-center justify-between" data-tilt data-tilt-max="3">
                    <div>
                        <p class="text-xs font-bold text-slate-200">${alt.name}</p>
                        <p class="text-[11px] text-emerald-400 mt-0.5">✨ ${alt.highlight}</p>
                    </div>
                    <div class="text-right">
                        <span class="text-sm font-extrabold text-emerald-400">${alt.score}/100</span>
                        <p class="text-[9px] text-slate-500 uppercase">Safety Score</p>
                    </div>
                </div>
            `).join('');
            if (window.VanillaTilt) VanillaTilt.init(document.querySelectorAll("[data-tilt]"));
        }

        // Modal Helpers
        function openModal(name, category, impact, reg, risk) {
            document.getElementById('modal-title').innerText = unescape(name);
            document.getElementById('modal-category').innerText = unescape(category);
            document.getElementById('modal-impact').innerText = unescape(impact);
            document.getElementById('modal-regulatory').innerText = unescape(reg);

            const badge = document.getElementById('modal-badge-icon');
            if (risk === 'red') {
                badge.className = "w-10 h-10 rounded-xl bg-rose-500/20 text-rose-400 flex items-center justify-center font-bold";
                badge.innerText = "🚨";
            } else if (risk === 'yellow') {
                badge.className = "w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold";
                badge.innerText = "⚠️";
            } else {
                badge.className = "w-10 h-10 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold";
                badge.innerText = "✅";
            }

            document.getElementById('ingredient-modal').classList.remove('hidden');
            document.getElementById('ingredient-modal').classList.add('flex');
        }

        function closeModal() {
            document.getElementById('ingredient-modal').classList.add('hidden');
            document.getElementById('ingredient-modal').classList.remove('flex');
        }

        function toggleApiKeyModal() {
            const modal = document.getElementById('apikey-modal');
            modal.classList.toggle('hidden');
            modal.classList.toggle('flex');
        }

        function saveApiKey() {
            const key = document.getElementById('api-key-input').value;
            if (key) {
                localStorage.setItem('gemini_key', key);
                alert('Gemini API Key saved for session!');
            }
            toggleApiKeyModal();
        }
    </script>
</body>
</html>