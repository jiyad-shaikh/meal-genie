import { useEffect, useMemo, useState } from 'react'
import { NavLink, Navigate, Route, Routes } from 'react-router-dom'
import { useRegisterSW } from 'virtual:pwa-register/react'

const API_BASE = import.meta.env.VITE_API_BASE || ''
const WHATSAPP_NUMBER = '917045475886'
const inputClass =
  'w-full rounded-xl border border-brand-300/55 bg-white px-3 py-3 text-sm text-brand-900 outline-none transition focus:border-brand-500 focus:ring-2 focus:ring-brand-300/45 dark:border-brand-400/35 dark:bg-[#0c1b15] dark:text-emerald-50 dark:focus:border-brand-300 dark:focus:ring-brand-400/30'

const fallbackMenuItems = [
  { id: 1, name: 'Chicken Masala Oats', type: 'non-veg', mealTime: 'breakfast', benefit: 'Lean protein plus complex carbs for steady morning energy.', nutrition: { calories: 450, protein: 35, carbs: 35, fats: 15 }, price: 149, image: '/static/images/chicken_masala_oats.jpg' },
  { id: 2, name: 'Mass Gainer Smoothie', type: 'veg', mealTime: 'snacks', benefit: 'Calorie-dense and quick for busy schedules.', nutrition: { calories: 510, protein: 18, carbs: 52, fats: 20 }, price: 189, image: '/static/images/smoothie.jpeg' },
  { id: 3, name: 'Paneer Bhurji + Roti + Bhindi', type: 'veg', mealTime: 'lunch', benefit: 'Balanced macros with high satiety and fiber.', nutrition: { calories: 520, protein: 30, carbs: 40, fats: 20 }, price: 179, image: '/static/images/paneer_bhurji.jpg' },
  { id: 4, name: 'Tandoori Chicken + Sweet Potato', type: 'non-veg', mealTime: 'dinner', benefit: 'Protein-rich recovery meal with slow carbs.', nutrition: { calories: 570, protein: 42, carbs: 38, fats: 22 }, price: 199, image: '/static/images/tandoori_chicken.png' },
  { id: 5, name: 'Curd Bowl with Chia & Fruits', type: 'veg', mealTime: 'snacks', benefit: 'Gut-friendly and light but filling.', nutrition: { calories: 180, protein: 10, carbs: 15, fats: 6 }, price: 119, image: '/static/images/curd_bowl.png' },
  { id: 6, name: 'Grilled Chicken + Boiled Veg Plate', type: 'non-veg', mealTime: 'dinner', benefit: 'Clean plate for fat loss without low energy.', nutrition: { calories: 420, protein: 35, carbs: 20, fats: 18 }, price: 199, image: '/static/images/grilled_chicken_boiled_veg_plate.png' },
]

const fallbackOptions = {
  goals: [{ value: 'general_health', label: 'General Health' }, { value: 'weight_loss', label: 'Weight Loss' }, { value: 'muscle_gain', label: 'Muscle Gain' }],
  preferences: [{ value: 'vegetarian', label: 'Vegetarian' }, { value: 'non-vegetarian', label: 'Non-Vegetarian' }, { value: 'jain', label: 'Jain' }],
  genders: [{ value: 'male', label: 'Male' }, { value: 'female', label: 'Female' }],
  activities: [{ value: 'sedentary', label: 'Sedentary' }, { value: 'moderate', label: 'Moderate' }, { value: 'active', label: 'Active' }],
  plan_durations: [
    { value: '1-day', label: '1-Day Trial', price: 0, available: true },
    { value: '3-day-premium', label: '3-Day Kickstart', price: 199, available: false },
    { value: '7-day-premium', label: '7-Day Full Immersion', price: 499, available: false },
  ],
}

const faqItems = [
  {
    question: 'How does Meal Genie generate my plan?',
    answer: 'We use your age, food preference, activity level, and fitness goal to map you to a practical daily plan from our nutrition dataset.',
  },
  {
    question: 'Can I use this if I am vegetarian?',
    answer: 'Yes. The plan supports vegetarian, non-vegetarian, and Jain preferences.',
  },
  {
    question: 'Are premium plans live right now?',
    answer: 'Not yet. In this phase, 1-day trial remains available while paid plans are being prepared.',
  },
  {
    question: 'Will payments be added soon?',
    answer: 'Yes. The React flow is prepared for upcoming payment integration after this migration phase.',
  },
]

function App() {
  const [theme, setTheme] = useState(() => localStorage.getItem('mg-theme') || 'dark')
  const [mobileOpen, setMobileOpen] = useState(false)
  const [promptEvent, setPromptEvent] = useState(null)
  const {
    needRefresh: [needRefresh, setNeedRefresh],
    offlineReady: [offlineReady, setOfflineReady],
    updateServiceWorker,
  } = useRegisterSW()

  useEffect(() => {
    const dark = theme === 'dark'
    document.documentElement.classList.toggle('dark', dark)
    document.documentElement.style.colorScheme = dark ? 'dark' : 'light'
    localStorage.setItem('mg-theme', theme)
  }, [theme])

  useEffect(() => {
    const onBeforeInstall = (event) => {
      event.preventDefault()
      setPromptEvent(event)
    }
    window.addEventListener('beforeinstallprompt', onBeforeInstall)
    window.addEventListener('appinstalled', () => setPromptEvent(null))
    return () => window.removeEventListener('beforeinstallprompt', onBeforeInstall)
  }, [])

  return (
    <div className="min-h-screen bg-brand-50 text-slate-900 transition-colors duration-300 dark:bg-[#071712] dark:text-emerald-50">
      <div className="mx-auto flex min-h-screen w-full max-w-6xl flex-col px-3 pb-8 pt-3 sm:px-4">
        <TopNav
          theme={theme}
          mobileOpen={mobileOpen}
          onClose={() => setMobileOpen(false)}
          onToggleMobile={() => setMobileOpen((v) => !v)}
          onToggleTheme={() => setTheme((v) => (v === 'dark' ? 'light' : 'dark'))}
        />

        <div className="flex-1">
          <Routes>
            <Route path="/" element={<Home theme={theme} />} />
            <Route path="/menu" element={<Menu theme={theme} />} />
            <Route path="/plan" element={<Plan theme={theme} />} />
            <Route path="/pricing" element={<Pricing theme={theme} />} />
            <Route path="/faq" element={<Faq theme={theme} />} />
            <Route path="/about" element={<About theme={theme} />} />
            <Route path="/contact" element={<Contact theme={theme} />} />
            <Route path="/privacy-policy" element={<PrivacyPolicy theme={theme} />} />
            <Route path="/privacy" element={<PrivacyPolicy theme={theme} />} />
            <Route path="/terms-of-service" element={<TermsOfService theme={theme} />} />
            <Route path="/terms" element={<TermsOfService theme={theme} />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </div>

        <Footer theme={theme} />
      </div>

      {(promptEvent || needRefresh || offlineReady) && (
        <div className="fixed bottom-4 left-3 right-3 z-40 rounded-2xl border border-brand-400/45 bg-white/95 p-3 shadow-soft dark:border-brand-400/30 dark:bg-[#0f231b]/95 sm:left-auto sm:right-4 sm:w-[360px]">
          <p className="text-sm font-semibold text-brand-800 dark:text-brand-100">
            {needRefresh ? 'A new version is ready.' : offlineReady ? 'App ready for offline use.' : 'Install Meal Genie for faster access.'}
          </p>
          <div className="mt-3 flex flex-wrap gap-2">
            {promptEvent && (
              <button
                type="button"
                onClick={async () => {
                  promptEvent.prompt()
                  await promptEvent.userChoice
                  setPromptEvent(null)
                }}
                className="rounded-lg border border-brand-600 bg-brand-600 px-3 py-2 text-xs font-bold text-white transition hover:bg-brand-700 dark:border-brand-400 dark:bg-brand-400 dark:text-[#053423] dark:hover:bg-brand-300"
              >
                Install
              </button>
            )}
            {needRefresh && (
              <button
                type="button"
                onClick={() => updateServiceWorker(true)}
                className="rounded-lg border border-brand-600 bg-brand-600 px-3 py-2 text-xs font-bold text-white transition hover:bg-brand-700 dark:border-brand-400 dark:bg-brand-400 dark:text-[#053423] dark:hover:bg-brand-300"
              >
                Refresh
              </button>
            )}
            <button
              type="button"
              onClick={() => {
                setNeedRefresh(false)
                setOfflineReady(false)
              }}
              className="rounded-lg border border-brand-400/50 bg-brand-100 px-3 py-2 text-xs font-bold text-brand-800 transition hover:bg-brand-200 dark:bg-brand-500/15 dark:text-brand-100 dark:hover:bg-brand-500/25"
            >
              Dismiss
            </button>
          </div>
        </div>
      )}
    </div>
  )
}

function TopNav({ theme, mobileOpen, onClose, onToggleMobile, onToggleTheme }) {
  const isDark = theme === 'dark'
  return (
    <header
      className={`sticky top-2 z-30 rounded-2xl border px-3 py-3 shadow-soft backdrop-blur ${
        isDark ? 'border-[#3adf95]/45 bg-[#0a1f18]' : 'border-brand-300/45 bg-white/95'
      }`}
    >
      <div className="flex items-center justify-between gap-3">
        <NavLink to="/" onClick={onClose} className="flex items-center gap-2">
          <img src="/logo-192.png" alt="Meal Genie" className="h-9 w-9 rounded-lg border border-brand-400/30 object-cover" />
          <span className={`brand-title text-xl font-extrabold ${isDark ? 'text-[#f7fff9]' : 'text-brand-700'}`}>Meal Genie</span>
        </NavLink>

        <nav className="hidden items-center gap-1 md:flex">
          <NavItem to="/" theme={theme}>Home</NavItem>
          <NavItem to="/menu" theme={theme}>Menu</NavItem>
          <NavItem to="/plan" theme={theme}>Get Plan</NavItem>
          <NavItem to="/pricing" theme={theme}>Pricing</NavItem>
          <NavItem to="/about" theme={theme}>About</NavItem>
          <NavItem to="/faq" theme={theme}>FAQ</NavItem>
          <NavItem to="/contact" theme={theme}>Contact</NavItem>
        </nav>

        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={onToggleTheme}
            className={`hidden h-11 w-11 items-center justify-center rounded-xl border transition sm:inline-flex ${
              isDark
                ? 'border-[#48e7a0]/50 bg-[#164435] text-[#f5fff9] hover:bg-[#1e5945]'
                : 'border-brand-400/45 bg-brand-100 text-brand-800 hover:bg-brand-200'
            }`}
            title={`Switch to ${isDark ? 'light' : 'dark'} mode`}
            aria-label={`Switch to ${isDark ? 'light' : 'dark'} mode`}
          >
            <ThemeModeIcon theme={theme} />
          </button>
          <button
            type="button"
            onClick={onToggleTheme}
            className={`inline-flex h-11 w-11 items-center justify-center rounded-xl border transition sm:hidden ${
              isDark
                ? 'border-[#48e7a0]/55 bg-[#164435] text-[#f5fff9] hover:bg-[#1e5945]'
                : 'border-brand-500/60 bg-brand-100 text-brand-800 hover:bg-brand-200'
            }`}
            title={`Switch to ${isDark ? 'light' : 'dark'} mode`}
            aria-label={`Switch to ${isDark ? 'light' : 'dark'} mode`}
          >
            <ThemeModeIcon theme={theme} />
          </button>
          <button
            type="button"
            className={`inline-flex h-11 w-11 items-center justify-center rounded-xl border transition md:hidden ${
              isDark
                ? 'border-[#48e7a0]/55 text-[#f7fff9] hover:bg-[#1d4f3d]'
                : 'border-brand-500/60 text-brand-700 hover:bg-brand-100'
            }`}
            onClick={onToggleMobile}
            aria-label="Toggle menu"
          >
            <div className="space-y-1">
              <span className={`block h-0.5 w-5 bg-current transition ${mobileOpen ? 'translate-y-1.5 rotate-45' : ''}`} />
              <span className={`block h-0.5 w-5 bg-current transition ${mobileOpen ? 'opacity-0' : ''}`} />
              <span className={`block h-0.5 w-5 bg-current transition ${mobileOpen ? '-translate-y-1.5 -rotate-45' : ''}`} />
            </div>
          </button>
        </div>
      </div>

      {mobileOpen && (
        <nav
          className={`mt-3 grid gap-2 rounded-xl border px-2 py-2 md:hidden ${
            isDark ? 'border-[#49e9a3]/45 bg-[#103124]' : 'border-brand-200/80 bg-white'
          }`}
        >
          <NavItem to="/" onClick={onClose} theme={theme}>Home</NavItem>
          <NavItem to="/menu" onClick={onClose} theme={theme}>Menu</NavItem>
          <NavItem to="/plan" onClick={onClose} theme={theme}>Get Plan</NavItem>
          <NavItem to="/pricing" onClick={onClose} theme={theme}>Pricing</NavItem>
          <NavItem to="/about" onClick={onClose} theme={theme}>About</NavItem>
          <NavItem to="/faq" onClick={onClose} theme={theme}>FAQ</NavItem>
          <NavItem to="/contact" onClick={onClose} theme={theme}>Contact</NavItem>
        </nav>
      )}
    </header>
  )
}

function ThemeModeIcon({ theme }) {
  const isDark = theme === 'dark'

  if (isDark) {
    return (
      <svg viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
        <circle cx="12" cy="12" r="4.2" />
        <path d="M12 2.5V5.2" strokeLinecap="round" />
        <path d="M12 18.8V21.5" strokeLinecap="round" />
        <path d="M2.5 12H5.2" strokeLinecap="round" />
        <path d="M18.8 12H21.5" strokeLinecap="round" />
        <path d="M5.1 5.1L7 7" strokeLinecap="round" />
        <path d="M17 17L18.9 18.9" strokeLinecap="round" />
        <path d="M17 7L18.9 5.1" strokeLinecap="round" />
        <path d="M5.1 18.9L7 17" strokeLinecap="round" />
      </svg>
    )
  }

  return (
    <svg viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="1.8" aria-hidden="true">
      <path d="M20.7 14.2a8.5 8.5 0 1 1-10.9-10.9 7 7 0 1 0 10.9 10.9Z" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  )
}

function NavItem({ to, children, onClick, theme }) {
  const isDark = theme === 'dark'
  return (
    <NavLink
      to={to}
      onClick={onClick}
      className={({ isActive }) =>
        `rounded-xl px-3 py-2 text-sm font-semibold transition ${
          isActive
            ? isDark
              ? 'bg-[#43d988] text-[#06281b]'
              : 'bg-brand-600 text-white'
            : isDark
              ? 'text-[#dcffef] hover:bg-[#1f5441] hover:text-white'
              : 'text-slate-700 hover:bg-brand-100'
        }`
      }
    >
      {children}
    </NavLink>
  )
}

function Home({ theme }) {
  const isDark = theme === 'dark'
  const sectionShell = isDark ? 'border-[#2e624d] bg-[#0f2a20]' : 'border-brand-300/40 bg-white/92'
  const bodyText = isDark ? 'text-[#d5f4e4]' : 'text-slate-700'
  const mutedText = isDark ? 'text-[#b8decf]' : 'text-slate-500'

  return (
    <main className="mt-3 space-y-4 sm:space-y-5">
      <section className="hero-shell rounded-[28px] border border-brand-300/45 bg-gradient-to-br from-[#0a3326] via-[#0f6b4e] to-[#19b172] p-4 shadow-soft sm:p-6 dark:border-brand-400/30">
        <div className="hero-glow" />
        <div className="relative z-10">
          <p className="text-[11px] font-semibold uppercase tracking-[0.17em] text-emerald-100/90 sm:text-xs sm:tracking-[0.2em]">Scheduled Meal Subscriptions</p>
          <h1 className="brand-title mt-1 max-w-2xl text-3xl font-extrabold leading-tight text-white drop-shadow-[0_4px_12px_rgba(0,0,0,0.25)] sm:mt-2 sm:text-5xl">
            Meal Genie
          </h1>
          <p className="mt-2 max-w-xl text-xs leading-relaxed text-emerald-50/95 sm:mt-3 sm:text-base">
            Home-style, clean, and hygienic meals for fat loss, muscle gain, and daily wellness with scheduled delivery slots.
          </p>
          <div className="mt-4 grid grid-cols-2 gap-2 sm:mt-5 sm:flex sm:flex-row sm:gap-3">
            <NavLink to="/plan" className="inline-flex items-center justify-center rounded-xl border border-[#dffef0]/45 bg-[#ffffff] px-3 py-2.5 text-sm font-bold text-brand-800 shadow-[0_8px_20px_rgba(4,34,24,0.2)] transition hover:bg-brand-100 sm:rounded-2xl sm:px-6 sm:py-3 sm:text-base">Get My Plan</NavLink>
            <NavLink to="/menu" className="inline-flex items-center justify-center rounded-xl border border-[#dffef0]/45 bg-[#0b3f2f]/90 px-3 py-2.5 text-sm font-bold text-emerald-50 transition hover:bg-[#0e4a38] sm:rounded-2xl sm:px-6 sm:py-3 sm:text-base">Explore Menu</NavLink>
          </div>
          <div className="mt-3 flex flex-wrap gap-2">
            <span className="rounded-full border border-white/35 bg-white/20 px-3 py-1 text-xs font-semibold text-emerald-50">Weekly & Monthly Plans</span>
            <span className="rounded-full border border-white/35 bg-white/20 px-3 py-1 text-xs font-semibold text-emerald-50">Scheduled Delivery Slots</span>
            <span className="hidden rounded-full border border-white/35 bg-white/20 px-3 py-1 text-xs font-semibold text-emerald-50 sm:inline-flex">Fresh Daily Preparation</span>
          </div>
        </div>
        <div className="relative z-10 mt-4 overflow-hidden rounded-xl border border-white/15 bg-[#04261b]/25 p-2 sm:mt-6 sm:rounded-2xl sm:p-3">
          <div className="dish-track">
            {[...fallbackMenuItems, ...fallbackMenuItems].map((meal, index) => (
              <div key={`${meal.id}-${index}`} className="dish-chip" aria-hidden="true">
                <img src={meal.image} alt={meal.name} loading="lazy" onError={(event) => { event.currentTarget.src = '/logo-192.png' }} />
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className={`rounded-3xl border p-4 shadow-soft sm:p-6 ${sectionShell}`}>
        <div className="grid gap-4 md:grid-cols-2">
          <article className={`rounded-2xl border p-4 ${isDark ? 'border-[#2f6a53] bg-[#163629]' : 'border-brand-200/70 bg-brand-50'}`}>
            <h2 className={`brand-title text-2xl font-extrabold ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>What Meal Genie Offers</h2>
            <p className={`mt-2 text-sm leading-relaxed sm:text-base ${bodyText}`}>
              Meal Genie is built as a cloud-kitchen subscription service focused on consistent, practical nutrition you can follow daily.
            </p>
            <ul className={`mt-3 ml-5 list-disc space-y-1 text-sm ${bodyText}`}>
              <li>Customized guidance + menu-based execution</li>
              <li>Weekly and monthly subscription plans</li>
              <li>Prepared meals aligned with your goals</li>
            </ul>
          </article>
          <article className={`rounded-2xl border p-4 ${isDark ? 'border-[#2f6a53] bg-[#163629]' : 'border-brand-200/70 bg-brand-50'}`}>
            <h2 className={`brand-title text-2xl font-extrabold ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>Our Delivery Model</h2>
            <p className={`mt-2 text-sm leading-relaxed sm:text-base ${bodyText}`}>
              We deliver meals in planned time windows through a subscription workflow designed for quality and reliability.
            </p>
            <ul className={`mt-3 ml-5 list-disc space-y-1 text-sm ${bodyText}`}>
              <li>Scheduled delivery slots for routine consistency</li>
              <li>Structured prep for better meal quality</li>
              <li>Reliable weekly/monthly support for regular users</li>
            </ul>
          </article>
        </div>
      </section>

      <section className={`rounded-3xl border p-4 shadow-soft sm:p-6 ${sectionShell}`}>
        <h2 className={`brand-title text-3xl font-extrabold sm:text-4xl ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>How Subscription Delivery Works</h2>
        <p className={`mt-2 text-sm sm:text-base ${mutedText}`}>Simple flow built for consistency, not guesswork.</p>
        <div className="mt-4 grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
          {[
            { title: 'Share Your Goal', description: 'Tell us your age, activity, preference, and target through the plan form.' },
            { title: 'Get Meal Routine', description: 'We map you to a realistic meal structure and suitable menu direction.' },
            { title: 'Choose Subscription', description: 'Pick weekly or monthly format and submit your preferred schedule.' },
            { title: 'Receive Scheduled Meals', description: 'Fresh batches are prepared and delivered in your selected time window.' },
          ].map((step, index) => (
            <article key={step.title} className={`rounded-2xl border p-4 ${isDark ? 'border-[#2f6a53] bg-[#163629]' : 'border-brand-200/70 bg-brand-50'}`}>
              <div className={`inline-flex h-8 w-8 items-center justify-center rounded-full text-sm font-extrabold ${isDark ? 'bg-[#66efb6] text-[#032116]' : 'bg-brand-600 text-white'}`}>
                {index + 1}
              </div>
              <h3 className={`mt-3 text-lg font-extrabold ${isDark ? 'text-[#e5fff3]' : 'text-brand-800'}`}>{step.title}</h3>
              <p className={`mt-2 text-sm leading-relaxed ${bodyText}`}>{step.description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className={`rounded-3xl border p-4 shadow-soft sm:p-6 ${sectionShell}`}>
        <h2 className={`brand-title text-3xl font-extrabold sm:text-4xl ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>Plans Built For Daily Routine</h2>
        <div className="mt-4 grid gap-3 md:grid-cols-3">
          {[
            { name: 'Starter Trial', duration: '1 Day', detail: 'Ideal to test taste, quality, and fit before subscribing.' },
            { name: 'Weekly Subscription', duration: '7 Days', detail: 'Best for working professionals who want structured meal support.' },
            { name: 'Monthly Subscription', duration: '30 Days', detail: 'Designed for long-term body composition and habit goals.' },
          ].map((plan) => (
            <article key={plan.name} className={`rounded-2xl border p-4 ${isDark ? 'border-[#2f6a53] bg-[#163629]' : 'border-brand-200/70 bg-brand-50'}`}>
              <p className={`text-xs font-semibold uppercase tracking-[0.15em] ${isDark ? 'text-[#b8decf]' : 'text-slate-500'}`}>{plan.duration}</p>
              <h3 className={`mt-2 text-xl font-extrabold ${isDark ? 'text-[#e5fff3]' : 'text-brand-800'}`}>{plan.name}</h3>
              <p className={`mt-2 text-sm leading-relaxed ${bodyText}`}>{plan.detail}</p>
            </article>
          ))}
        </div>
      </section>

      <section className={`rounded-3xl border p-4 shadow-soft sm:p-6 ${sectionShell}`}>
        <h2 className={`brand-title text-3xl font-extrabold sm:text-4xl ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>Our Kitchen Promise</h2>
        <div className="mt-4 grid gap-3 md:grid-cols-3">
          {[
            { title: 'Home-Style Cooking', text: 'Balanced meals designed to be practical for everyday Indian lifestyles.' },
            { title: 'Clean & Hygienic Prep', text: 'Controlled preparation flow with food-safety discipline in every batch.' },
            { title: 'Fresh Quality Inputs', text: 'Ingredient quality and meal consistency are prioritized over rush delivery.' },
          ].map((item) => (
            <article key={item.title} className={`rounded-2xl border p-4 ${isDark ? 'border-[#2f6a53] bg-[#163629]' : 'border-brand-200/70 bg-brand-50'}`}>
              <h3 className={`text-lg font-extrabold ${isDark ? 'text-[#cbf8e0]' : 'text-brand-700'}`}>{item.title}</h3>
              <p className={`mt-2 text-sm leading-relaxed ${bodyText}`}>{item.text}</p>
            </article>
          ))}
        </div>
      </section>

      <section className={`rounded-3xl border p-4 shadow-soft sm:p-6 ${sectionShell}`}>
        <h2 className={`brand-title text-3xl font-extrabold sm:text-4xl ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>Popular Meals In Rotation</h2>
        <p className={`mt-2 text-sm sm:text-base ${mutedText}`}>Examples from our current menu lineup.</p>
        <div className="mt-4 grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
          {fallbackMenuItems.slice(0, 3).map((meal) => (
            <article key={meal.id} className={`overflow-hidden rounded-2xl border ${isDark ? 'border-[#2f6a53] bg-[#163629]' : 'border-brand-200/70 bg-brand-50'}`}>
              <img src={meal.image} alt={meal.name} className="h-40 w-full object-cover" loading="lazy" onError={(event) => { event.currentTarget.src = '/logo-192.png' }} />
              <div className="p-4">
                <h3 className={`text-lg font-extrabold ${isDark ? 'text-[#e5fff3]' : 'text-brand-800'}`}>{meal.name}</h3>
                <p className={`mt-1 text-sm ${bodyText}`}>{meal.mealTime.toUpperCase()} | {meal.type.toUpperCase()}</p>
                <p className={`mt-1 text-sm ${bodyText}`}>{meal.nutrition.calories} kcal | {meal.nutrition.protein}g protein</p>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="rounded-3xl border border-brand-300/45 bg-gradient-to-r from-[#0a3326] via-[#0f6b4e] to-[#159b68] p-5 shadow-soft sm:p-6">
        <h2 className="brand-title text-3xl font-extrabold text-white sm:text-4xl">Ready To Start A Better Meal Routine?</h2>
        <p className="mt-2 max-w-3xl text-sm text-emerald-50/95 sm:text-base">
          Start with your personalized plan, then move to a practical weekly or monthly subscription model designed for consistent results.
        </p>
        <div className="mt-4 flex flex-col gap-3 sm:flex-row">
          <NavLink to="/plan" className="inline-flex items-center justify-center rounded-2xl border border-white/35 bg-white px-6 py-3 text-sm font-bold text-brand-800 transition hover:bg-brand-100 sm:text-base">Generate My Plan</NavLink>
          <NavLink to="/menu" className="inline-flex items-center justify-center rounded-2xl border border-white/35 bg-[#0b3f2f]/90 px-6 py-3 text-sm font-bold text-emerald-50 transition hover:bg-[#0e4a38] sm:text-base">See Menu & Subscription Options</NavLink>
          <NavLink to="/contact" className="inline-flex items-center justify-center rounded-2xl border border-white/35 bg-transparent px-6 py-3 text-sm font-bold text-emerald-50 transition hover:bg-white/10 sm:text-base">Talk To Team</NavLink>
        </div>
      </section>
    </main>
  )
}

function Menu({ theme }) {
  const isDark = theme === 'dark'
  const [query, setQuery] = useState('')
  const [typeFilter, setTypeFilter] = useState('all')
  const [mealTimeFilter, setMealTimeFilter] = useState('all')
  const [menuItems, setMenuItems] = useState(fallbackMenuItems)
  const [loading, setLoading] = useState(true)
  const [menuError, setMenuError] = useState('')

  useEffect(() => {
    let active = true
    fetch(`${API_BASE}/api/menu-items`)
      .then((res) => (res.ok ? res.json() : null))
      .then((data) => {
        if (active && data?.ok && Array.isArray(data.items) && data.items.length) {
          setMenuItems(data.items)
          setMenuError('')
        }
      })
      .catch(() => {
        if (active) {
          setMenuError('Using fallback menu data because live menu API is unavailable.')
        }
      })
      .finally(() => {
        if (active) {
          setLoading(false)
        }
      })

    return () => {
      active = false
    }
  }, [])

  const filtered = useMemo(() => menuItems.filter((meal) => {
    const s = query.trim().toLowerCase()
    const matchSearch = !s || meal.name.toLowerCase().includes(s) || meal.mealTime.toLowerCase().includes(s)
    return matchSearch && (typeFilter === 'all' || meal.type === typeFilter) && (mealTimeFilter === 'all' || meal.mealTime === mealTimeFilter)
  }), [menuItems, query, typeFilter, mealTimeFilter])

  return (
    <main className="mt-4 space-y-4">
      <section className={`rounded-3xl border p-4 shadow-soft ${isDark ? 'border-[#2e624d] bg-[#0f2a20]' : 'border-brand-300/40 bg-white/90'}`}>
        <div className={`search-wrap flex items-center gap-2 rounded-2xl border px-3 py-2 ${isDark ? 'border-[#2f6a53] bg-[#0b2018]' : 'border-brand-300/45 bg-white'}`}>
          <svg className={`h-5 w-5 ${isDark ? 'text-[#d8fff0]' : 'text-brand-700'}`} viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <circle cx="11" cy="11" r="7" stroke="currentColor" strokeWidth="2" />
            <path d="M20 20L16.8 16.8" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
          </svg>
          <input
            type="search"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Search meals, ingredients, or nutrition goals"
            className={`w-full border-none bg-transparent text-sm font-medium outline-none ${isDark ? 'text-[#ecfff5] placeholder:text-[#9dd8be]' : 'text-brand-900 placeholder:text-slate-500'}`}
          />
        </div>
      </section>
      {menuError && (
        <p className="rounded-xl border border-amber-300 bg-amber-50 px-3 py-2 text-sm font-medium text-amber-800 dark:border-amber-500/35 dark:bg-amber-500/10 dark:text-amber-200">
          {menuError}
        </p>
      )}
      <section className={`rounded-2xl border p-4 shadow-soft ${isDark ? 'border-[#2e624d] bg-[#0f2a20]' : 'border-brand-300/40 bg-white/90'}`}>
        <div className="mb-3 flex flex-wrap gap-2">
          {['all', 'veg', 'non-veg'].map((value) => {
            const active = typeFilter === value
            return (
              <button
                key={value}
                type="button"
                onClick={() => setTypeFilter(value)}
                className={`rounded-full border px-4 py-2 text-sm font-semibold transition-colors ${
                  active
                    ? isDark
                      ? 'border-[#66efb6] bg-[#66efb6] text-[#042114]'
                      : 'border-brand-700 bg-brand-700 text-white'
                    : isDark
                      ? 'border-[#2f6a53] bg-[#163629] text-[#e8fff4] hover:bg-[#1f4938]'
                      : 'border-brand-400 bg-white text-brand-800 hover:bg-brand-100'
                }`}
              >
                {value === 'all' ? 'All Types' : value === 'veg' ? 'Veg' : 'Non-Veg'}
              </button>
            )
          })}
        </div>

        <div className="flex flex-wrap gap-2">
          {['all', 'breakfast', 'lunch', 'dinner', 'snacks'].map((value) => {
            const active = mealTimeFilter === value
            return (
              <button
                key={value}
                type="button"
                onClick={() => setMealTimeFilter(value)}
                className={`rounded-full border px-4 py-2 text-sm font-semibold transition-colors ${
                  active
                    ? isDark
                      ? 'border-[#66efb6] bg-[#66efb6] text-[#042114]'
                      : 'border-brand-700 bg-brand-700 text-white'
                    : isDark
                      ? 'border-[#2f6a53] bg-[#163629] text-[#e8fff4] hover:bg-[#1f4938]'
                      : 'border-brand-400 bg-white text-brand-800 hover:bg-brand-100'
                }`}
              >
                {value === 'all' ? 'All Times' : value[0].toUpperCase() + value.slice(1)}
              </button>
            )
          })}
        </div>
      </section>
      <section className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
        {loading && (
          <p className={`rounded-2xl border p-4 text-sm ${isDark ? 'border-[#2e624d] bg-[#0f2a20] text-[#d8fff0]' : 'border-brand-300/40 bg-white/80 text-slate-600'}`}>
            Loading menu...
          </p>
        )}
        {!loading && filtered.length === 0 && (
          <p className={`rounded-2xl border p-4 text-sm ${isDark ? 'border-[#2e624d] bg-[#0f2a20] text-[#d8fff0]' : 'border-brand-300/40 bg-white/80 text-slate-600'}`}>
            No meals found for the selected filters.
          </p>
        )}
        {filtered.map((meal) => (
          <article key={meal.id} className={`overflow-hidden rounded-2xl border shadow-soft ${isDark ? 'border-[#2f6a53] bg-[#112f24]' : 'border-brand-300/45 bg-white'}`}>
            <img src={meal.image} alt={meal.name} className="h-44 w-full object-cover" loading="lazy" onError={(event) => { event.currentTarget.src = '/logo-192.png' }} />
            <div className="space-y-3 p-4">
              <h3 className={`text-lg font-extrabold ${isDark ? 'text-[#e5fff3]' : 'text-brand-700'}`}>{meal.name}</h3>
              <p className={`text-sm ${isDark ? 'text-[#c8f2de]' : 'text-slate-700'}`}>{meal.mealTime.toUpperCase()} | {meal.type.toUpperCase()}</p>
              <p className={`text-sm ${isDark ? 'text-[#c8f2de]' : 'text-slate-700'}`}>{meal.nutrition.calories} kcal | {meal.nutrition.protein}g P | {meal.nutrition.carbs}g C | {meal.nutrition.fats}g F</p>
              {meal.benefit && <p className={`text-sm ${isDark ? 'text-[#b9e8d2]' : 'text-slate-600'}`}>{meal.benefit}</p>}
              <div className="flex items-center justify-between"><span className={`text-lg font-extrabold ${isDark ? 'text-[#e5fff3]' : 'text-brand-800'}`}>Rs {meal.price}</span><a href={`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(`Hi, I would like to order ${meal.name}`)}`} target="_blank" rel="noreferrer" className={`rounded-xl border px-3 py-2 text-sm font-bold transition ${isDark ? 'border-[#66efb6] bg-[#66efb6] text-[#032116] hover:bg-[#7ef3c0]' : 'border-brand-600 bg-brand-600 text-white hover:bg-brand-700'}`}>Order</a></div>
            </div>
          </article>
        ))}
      </section>
    </main>
  )
}

function Faq({ theme }) {
  const isDark = theme === 'dark'
  const [openIndex, setOpenIndex] = useState(0)

  return (
    <main className="mt-4">
      <section className={`rounded-3xl border p-5 shadow-soft ${isDark ? 'border-[#2e624d] bg-[#0f2a20]' : 'border-brand-300/40 bg-white/92'}`}>
        <h2 className={`brand-title text-3xl font-extrabold sm:text-4xl ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>Frequently Asked Questions</h2>
        <div className="mt-4 space-y-3">
          {faqItems.map((item, index) => (
            <article key={item.question} className={`rounded-2xl border ${isDark ? 'border-[#2f6a53] bg-[#163629]' : 'border-brand-300/40 bg-brand-50'}`}>
              <button
                type="button"
                className="flex w-full items-center justify-between gap-3 px-4 py-3 text-left"
                onClick={() => setOpenIndex((prev) => (prev === index ? -1 : index))}
              >
                <span className={`text-sm font-bold sm:text-base ${isDark ? 'text-[#e8fff4]' : 'text-brand-800'}`}>{item.question}</span>
                <span className={`${isDark ? 'text-[#c7f7df]' : 'text-brand-700'}`}>{openIndex === index ? '-' : '+'}</span>
              </button>
              {openIndex === index && (
                <p className={`border-t px-4 py-3 text-sm ${isDark ? 'border-[#2f6a53] text-[#cdeedc]' : 'border-brand-200/70 text-slate-700'}`}>
                  {item.answer}
                </p>
              )}
            </article>
          ))}
        </div>
      </section>
    </main>
  )
}

function About({ theme }) {
  const isDark = theme === 'dark'
  return (
    <main className="mt-4">
      <section className={`rounded-3xl border p-5 shadow-soft sm:p-6 ${isDark ? 'border-[#2e624d] bg-[#0f2a20]' : 'border-brand-300/40 bg-white/92'}`}>
        <h2 className={`brand-title text-3xl font-extrabold sm:text-4xl ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>About Meal Genie</h2>
        <p className={`mt-3 text-sm leading-relaxed sm:text-base ${isDark ? 'text-[#d5f4e4]' : 'text-slate-700'}`}>
          Meal Genie helps users move from guesswork to practical nutrition. We focus on personalized plans, clean meal choices, and simple daily execution.
        </p>
        <div className="mt-4 grid gap-3 md:grid-cols-3">
          <InfoCard title="Personalized" text="Plans mapped to age, activity, and goals instead of one-size-fits-all charts." theme={theme} />
          <InfoCard title="Indian-Friendly" text="Meals are designed around familiar flavors and realistic local choices." theme={theme} />
          <InfoCard title="Execution-Focused" text="From generated plan to ordering flow, the journey is built for daily consistency." theme={theme} />
        </div>
      </section>
    </main>
  )
}

function Contact({ theme }) {
  const isDark = theme === 'dark'
  return (
    <main className="mt-4">
      <section className={`rounded-3xl border p-5 shadow-soft sm:p-6 ${isDark ? 'border-[#2e624d] bg-[#0f2a20]' : 'border-brand-300/40 bg-white/92'}`}>
        <h2 className={`brand-title text-3xl font-extrabold sm:text-4xl ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>Contact Meal Genie</h2>
        <p className={`mt-3 text-sm ${isDark ? 'text-[#d5f4e4]' : 'text-slate-700'}`}>
          For custom plans, partnerships, or support, reach us directly.
        </p>
        <div className="mt-4 grid gap-3 sm:grid-cols-2">
          <InfoCard title="WhatsApp" text="+91 70454 75886" theme={theme} />
          <InfoCard title="Email" text="mealgenie.fit@gmail.com" theme={theme} />
        </div>
        <div className="mt-4 flex flex-wrap gap-3">
          <a
            href={`https://wa.me/${WHATSAPP_NUMBER}`}
            target="_blank"
            rel="noreferrer"
            className={`rounded-xl border px-4 py-3 text-sm font-bold transition ${isDark ? 'border-[#66efb6] bg-[#66efb6] text-[#042114] hover:bg-[#7cf2be]' : 'border-brand-600 bg-brand-600 text-white hover:bg-brand-700'}`}
          >
            Chat on WhatsApp
          </a>
          <a
            href="mailto:mealgenie.fit@gmail.com"
            className={`rounded-xl border px-4 py-3 text-sm font-bold transition ${isDark ? 'border-[#5ec8a0] bg-[#113729] text-[#e7fff4] hover:bg-[#1a4b39]' : 'border-brand-500/60 bg-transparent text-brand-700 hover:bg-brand-100'}`}
          >
            Send Email
          </a>
        </div>
      </section>
    </main>
  )
}

function PrivacyPolicy({ theme }) {
  const isDark = theme === 'dark'
  const bodyText = isDark ? 'text-[#d5f4e4]' : 'text-slate-700'
  const linkClass = `underline underline-offset-4 ${isDark ? 'text-[#cbf8e0] hover:text-[#f2fff8]' : 'text-brand-700 hover:text-brand-600'}`
  const listClass = `ml-5 list-disc space-y-1 ${bodyText}`

  return (
    <main className="mt-4">
      <section className={`rounded-3xl border p-5 shadow-soft sm:p-6 ${isDark ? 'border-[#2e624d] bg-[#0f2a20]' : 'border-brand-300/40 bg-white/92'}`}>
        <h2 className={`brand-title text-3xl font-extrabold sm:text-4xl ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>Privacy Policy</h2>
        <p className={`mt-2 text-sm ${isDark ? 'text-[#b8decf]' : 'text-slate-500'}`}>Last updated: May 2025</p>

        <div className="mt-4 space-y-3">
          <LegalSection title="1. Introduction" theme={theme}>
            <p className={bodyText}>Welcome to Meal Genie. We are committed to protecting your privacy. This policy explains how we collect, use, and safeguard your information when you visit our website.</p>
          </LegalSection>

          <LegalSection title="2. Information We Collect" theme={theme}>
            <p className={bodyText}>We may collect personal information when you register, complete questionnaires, subscribe, or contact us.</p>
            <ul className={listClass}>
              <li>Name, email address, and phone number</li>
              <li>Dietary preferences and health goals</li>
              <li>Payment information for premium services</li>
            </ul>
            <p className={`mt-2 ${bodyText}`}>We also automatically collect technical data such as IP address, browser type, operating system, pages visited, and time spent on pages.</p>
          </LegalSection>

          <LegalSection title="3. How We Use Your Information" theme={theme}>
            <ul className={listClass}>
              <li>Create and deliver personalized meal plans</li>
              <li>Improve website performance and service quality</li>
              <li>Respond to support inquiries</li>
              <li>Process payments and maintain account security</li>
              <li>Send promotions with your consent</li>
              <li>Analyze usage trends and prevent fraud</li>
            </ul>
          </LegalSection>

          <LegalSection title="4. Google AdSense" theme={theme}>
            <p className={bodyText}>We may use Google AdSense for advertising. AdSense can use cookies to show personalized ads based on browsing behavior.</p>
            <ul className={`mt-2 ${listClass}`}>
              <li>Use cookies to serve personalized ads</li>
              <li>Collect information about visits to our and other websites</li>
              <li>Use this information to improve ad relevance</li>
            </ul>
            <p className={`mt-2 ${bodyText}`}>
              You can manage ad personalization at{' '}
              <a className={linkClass} href="https://adssettings.google.com" target="_blank" rel="noreferrer">
                Google Ads Settings
              </a>.
            </p>
          </LegalSection>

          <LegalSection title="5. Data Sharing and Disclosure" theme={theme}>
            <p className={bodyText}>We do not sell personal information. We may share data in the following cases:</p>
            <ul className={`mt-2 ${listClass}`}>
              <li>Service providers who help run our operations</li>
              <li>Google AdSense and related advertising partners</li>
              <li>Legal authorities when required by law</li>
            </ul>
          </LegalSection>

          <LegalSection title="6. Data Security" theme={theme}>
            <p className={bodyText}>We use reasonable security safeguards, but no internet-based transmission can be guaranteed 100% secure.</p>
          </LegalSection>

          <LegalSection title="7. Your Rights" theme={theme}>
            <ul className={listClass}>
              <li>Access, update, or request deletion of personal data</li>
              <li>Opt out of marketing messages</li>
              <li>Disable cookies in browser settings</li>
            </ul>
          </LegalSection>

          <LegalSection title="8. Changes to This Policy" theme={theme}>
            <p className={bodyText}>We may revise this policy periodically. Significant changes will be published on this page.</p>
          </LegalSection>

          <LegalSection title="9. Contact Us" theme={theme}>
            <p className={bodyText}>
              For questions about this Privacy Policy, use our{' '}
              <NavLink className={linkClass} to="/contact">
                contact page
              </NavLink>.
            </p>
          </LegalSection>
        </div>
      </section>
    </main>
  )
}

function TermsOfService({ theme }) {
  const isDark = theme === 'dark'
  const bodyText = isDark ? 'text-[#d5f4e4]' : 'text-slate-700'
  const listClass = `ml-5 list-disc space-y-1 ${bodyText}`
  const linkClass = `underline underline-offset-4 ${isDark ? 'text-[#cbf8e0] hover:text-[#f2fff8]' : 'text-brand-700 hover:text-brand-600'}`

  return (
    <main className="mt-4">
      <section className={`rounded-3xl border p-5 shadow-soft sm:p-6 ${isDark ? 'border-[#2e624d] bg-[#0f2a20]' : 'border-brand-300/40 bg-white/92'}`}>
        <h2 className={`brand-title text-3xl font-extrabold sm:text-4xl ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>Terms of Service</h2>
        <p className={`mt-2 text-sm ${isDark ? 'text-[#b8decf]' : 'text-slate-500'}`}>Last updated: May 2025</p>

        <div className="mt-4 space-y-3">
          <LegalSection title="1. Acceptance of Terms" theme={theme}>
            <p className={bodyText}>By accessing or using Meal Genie services, you agree to these Terms of Service.</p>
          </LegalSection>

          <LegalSection title="2. Service Description" theme={theme}>
            <p className={bodyText}>Meal Genie provides personalized meal planning based on user-provided preferences, goals, and related inputs.</p>
          </LegalSection>

          <LegalSection title="3. User Responsibilities" theme={theme}>
            <ul className={listClass}>
              <li>Provide accurate and complete information</li>
              <li>Use the service for personal, non-commercial use</li>
              <li>Keep account credentials secure</li>
              <li>Consult healthcare professionals before major diet changes</li>
            </ul>
          </LegalSection>

          <LegalSection title="4. Intellectual Property" theme={theme}>
            <p className={bodyText}>All meal plans and related content are protected by copyright and may not be copied or redistributed without permission.</p>
          </LegalSection>

          <LegalSection title="5. Payments and Refunds" theme={theme}>
            <ul className={listClass}>
              <li>Premium services require payment</li>
              <li>Digital products are non-refundable after delivery</li>
              <li>Subscriptions may be cancelled anytime with no prorated refund</li>
            </ul>
          </LegalSection>

          <LegalSection title="6. Disclaimer" theme={theme}>
            <p className={bodyText}>Meal Genie provides general dietary information, not medical advice. Results vary based on individual factors and adherence.</p>
          </LegalSection>

          <LegalSection title="7. Limitation of Liability" theme={theme}>
            <p className={bodyText}>Meal Genie is not liable for indirect, incidental, or consequential damages arising from service usage.</p>
          </LegalSection>

          <LegalSection title="8. Modifications" theme={theme}>
            <p className={bodyText}>We may update these terms at any time. Continued use indicates acceptance of revised terms.</p>
          </LegalSection>

          <LegalSection title="9. Governing Law" theme={theme}>
            <p className={bodyText}>These terms are governed by the laws of India, Maharashtra.</p>
          </LegalSection>

          <LegalSection title="10. Contact Information" theme={theme}>
            <p className={bodyText}>
              For questions about these terms, use our{' '}
              <NavLink className={linkClass} to="/contact">
                contact page
              </NavLink>.
            </p>
          </LegalSection>
        </div>
      </section>
    </main>
  )
}

function LegalSection({ title, theme, children }) {
  const isDark = theme === 'dark'
  return (
    <article className={`rounded-2xl border p-4 ${isDark ? 'border-[#2f6a53] bg-[#163629]' : 'border-brand-200/70 bg-brand-50'}`}>
      <h3 className={`text-base font-extrabold ${isDark ? 'text-[#cbf8e0]' : 'text-brand-700'}`}>{title}</h3>
      <div className="mt-2 text-sm leading-relaxed">{children}</div>
    </article>
  )
}

function InfoCard({ title, text, theme }) {
  const isDark = theme === 'dark'
  return (
    <article className={`rounded-2xl border p-4 ${isDark ? 'border-[#2f6a53] bg-[#163629]' : 'border-brand-200/70 bg-brand-50'}`}>
      <h3 className={`text-sm font-extrabold uppercase tracking-[0.14em] ${isDark ? 'text-[#cbf8e0]' : 'text-brand-700'}`}>{title}</h3>
      <p className={`mt-2 text-sm ${isDark ? 'text-[#d5f4e4]' : 'text-slate-700'}`}>{text}</p>
    </article>
  )
}

function Footer({ theme }) {
  const isDark = theme === 'dark'
  return (
    <footer className={`mt-6 rounded-2xl border p-4 shadow-soft ${isDark ? 'border-[#2e624d] bg-[#0f2a20]' : 'border-brand-400/30 bg-white/90'}`}>
      <div className="flex flex-wrap justify-center gap-x-4 gap-y-2 text-sm font-semibold sm:gap-x-6">
        <NavLink className={`underline underline-offset-4 ${isDark ? 'text-[#cbf8e0] hover:text-[#f2fff8]' : 'text-brand-700 hover:text-brand-600'}`} to="/faq">FAQ</NavLink>
        <NavLink className={`underline underline-offset-4 ${isDark ? 'text-[#cbf8e0] hover:text-[#f2fff8]' : 'text-brand-700 hover:text-brand-600'}`} to="/about">About Us</NavLink>
        <NavLink className={`underline underline-offset-4 ${isDark ? 'text-[#cbf8e0] hover:text-[#f2fff8]' : 'text-brand-700 hover:text-brand-600'}`} to="/contact">Contact</NavLink>
      </div>
      <p className={`mt-3 text-center text-xs ${isDark ? 'text-[#b8decf]' : 'text-slate-500'}`}>(c) 2026 Meal Genie. All rights reserved.</p>
      <div className="mt-3 flex items-center justify-center gap-8 text-sm font-semibold">
        <NavLink className={`underline underline-offset-4 ${isDark ? 'text-[#cbf8e0] hover:text-[#f2fff8]' : 'text-brand-700 hover:text-brand-600'}`} to="/privacy-policy">Privacy Policy</NavLink>
        <NavLink className={`underline underline-offset-4 ${isDark ? 'text-[#cbf8e0] hover:text-[#f2fff8]' : 'text-brand-700 hover:text-brand-600'}`} to="/terms-of-service">Terms of Service</NavLink>
      </div>
    </footer>
  )
}

function Plan({ theme }) {
  const isDark = theme === 'dark'
  const [options, setOptions] = useState(fallbackOptions)
  const [step, setStep] = useState(1)
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState('')
  const [result, setResult] = useState(null)
  const [form, setForm] = useState({ age: '', gender: '', preference: '', activity: '', height: '', weight: '', goal: '', plan_duration: '1-day' })

  useEffect(() => {
    let active = true
    fetch(`${API_BASE}/api/plan-options`).then((res) => (res.ok ? res.json() : null)).then((data) => {
      if (active && data?.goals) setOptions(data)
    }).catch(() => {})
    return () => { active = false }
  }, [])

  const suggestedGoal = useMemo(() => {
    const h = Number(form.height)
    const w = Number(form.weight)
    if (!h || !w) return ''
    const bmi = w / ((h / 100) * (h / 100))
    if (bmi < 18.5) return 'muscle_gain'
    if (bmi >= 25) return 'weight_loss'
    return 'general_health'
  }, [form.height, form.weight])

  useEffect(() => {
    if (step === 2 && suggestedGoal && !form.goal) {
      setForm((prev) => ({ ...prev, goal: suggestedGoal }))
    }
  }, [form.goal, step, suggestedGoal])

  const validateForStep = (stepNumber) => {
    if (stepNumber === 1) {
      if (!form.age || Number(form.age) < 10 || Number(form.age) > 90) return 'Enter a valid age between 10 and 90.'
      if (!form.gender || !form.preference || !form.activity) return 'Complete all Step 1 fields to continue.'
    }
    if (stepNumber === 2) {
      if (!form.height || !form.weight || Number(form.height) < 100 || Number(form.weight) < 30) return 'Enter valid height and weight to continue.'
      if (!form.goal) return 'Choose your fitness goal to continue.'
    }
    if (stepNumber === 3 && !form.plan_duration) return 'Select a plan duration.'
    return ''
  }

  const onSubmit = async (event) => {
    event.preventDefault()
    const validation = validateForStep(1) || validateForStep(2) || validateForStep(3)
    if (validation) {
      setError(validation)
      return
    }
    if (form.plan_duration !== '1-day') {
      setError('Premium durations are not active yet. Please select the 1-Day Trial.')
      return
    }
    setSubmitting(true)
    setError('')
    try {
      const res = await fetch(`${API_BASE}/api/meal-plan`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ age: Number(form.age), gender: form.gender, preference: form.preference, activity: form.activity, goal: form.goal }),
      })
      const data = await res.json()
      if (!res.ok || !data.ok) {
        setResult(null)
        setError(Object.values(data?.errors || {})[0] || 'Could not generate a meal plan.')
      } else {
        setResult(data)
      }
    } catch {
      setError('Network issue while generating your plan. Make sure Flask backend is running.')
      setResult(null)
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <main className="mt-4 space-y-4">
      <section className="rounded-3xl border border-brand-300/40 bg-white/92 p-4 shadow-soft dark:border-brand-400/20 dark:bg-[#0f231b]/92 sm:p-6">
        <h2 className="brand-title text-3xl font-extrabold text-brand-700 dark:text-brand-200 sm:text-4xl">Your Personalized Meal Plan Journey</h2>
        <div className="mt-4 flex items-center gap-2 sm:max-w-md">{[1, 2, 3].map((value) => <div key={value} className="flex flex-1 items-center"><div className={`h-9 w-9 rounded-full border text-center text-sm font-extrabold leading-9 ${value <= step ? 'border-brand-600 bg-brand-600 text-white dark:border-brand-400 dark:bg-brand-400 dark:text-[#053423]' : 'border-brand-300 text-brand-700 dark:border-brand-400/30 dark:text-brand-200'}`}>{value}</div>{value < 3 && <div className={`h-[2px] flex-1 ${value < step ? 'bg-brand-600 dark:bg-brand-400' : 'bg-brand-200 dark:bg-brand-400/25'}`} />}</div>)}</div>
        {error && <p className="mt-4 rounded-xl border border-red-300 bg-red-50 px-3 py-2 text-sm font-medium text-red-700 dark:border-red-500/35 dark:bg-red-500/10 dark:text-red-200">{error}</p>}
        <form className="mt-4 space-y-4" onSubmit={onSubmit}>
          {step === 1 && (
            <div className="grid gap-3 sm:grid-cols-2">
              <input type="number" min="10" max="90" placeholder="Age" value={form.age} onChange={(event) => setForm((prev) => ({ ...prev, age: event.target.value }))} className={inputClass} />
              <select value={form.gender} onChange={(event) => setForm((prev) => ({ ...prev, gender: event.target.value }))} className={inputClass}><option value="">Gender</option>{options.genders.map((o) => <option key={o.value} value={o.value}>{o.label}</option>)}</select>
              <select value={form.preference} onChange={(event) => setForm((prev) => ({ ...prev, preference: event.target.value }))} className={inputClass}><option value="">Food Preference</option>{options.preferences.map((o) => <option key={o.value} value={o.value}>{o.label}</option>)}</select>
              <select value={form.activity} onChange={(event) => setForm((prev) => ({ ...prev, activity: event.target.value }))} className={inputClass}><option value="">Activity</option>{options.activities.map((o) => <option key={o.value} value={o.value}>{o.label}</option>)}</select>
            </div>
          )}
          {step === 2 && (
            <div className="grid gap-3 sm:grid-cols-2">
              <input type="number" min="100" max="230" placeholder="Height (cm)" value={form.height} onChange={(event) => setForm((prev) => ({ ...prev, height: event.target.value }))} className={inputClass} />
              <input type="number" min="30" max="200" placeholder="Weight (kg)" value={form.weight} onChange={(event) => setForm((prev) => ({ ...prev, weight: event.target.value }))} className={inputClass} />
              <input readOnly value={suggestedGoal ? `Suggested: ${suggestedGoal.replace('_', ' ')}` : 'Suggested goal appears after height/weight'} className={`${inputClass} opacity-80`} />
              <select value={form.goal} onChange={(event) => setForm((prev) => ({ ...prev, goal: event.target.value }))} className={inputClass}><option value="">Fitness Goal</option>{options.goals.map((o) => <option key={o.value} value={o.value}>{o.label}</option>)}</select>
            </div>
          )}
          {step === 3 && (
            <div className="grid gap-3 md:grid-cols-3">
              {options.plan_durations.map((d) => {
                const isSelected = form.plan_duration === d.value
                const cardClass = isSelected
                  ? isDark
                    ? 'border-[#66efb6] bg-[#154735]'
                    : 'border-brand-600 bg-brand-100'
                  : isDark
                    ? 'border-[#2f6a53] bg-[#0f251c]'
                    : 'border-brand-300/55 bg-brand-50'
                const metaClass = isSelected
                  ? isDark
                    ? 'text-[#aef5cc]'
                    : 'text-brand-700'
                  : isDark
                    ? 'text-[#8fd9b6]'
                    : 'text-slate-500'
                const titleClass = isSelected
                  ? isDark
                    ? 'text-[#f0fff8]'
                    : 'text-brand-800'
                  : isDark
                    ? 'text-[#ddfcea]'
                    : 'text-brand-800'
                const priceClass = isSelected
                  ? isDark
                    ? 'text-[#dff9eb]'
                    : 'text-slate-700'
                  : isDark
                    ? 'text-[#c1ecd8]'
                    : 'text-slate-700'

                return (
                  <label key={d.value} className={`cursor-pointer rounded-2xl border p-4 transition ${cardClass}`}>
                    <input
                      type="radio"
                      className="sr-only"
                      checked={isSelected}
                      onChange={() => setForm((prev) => ({ ...prev, plan_duration: d.value }))}
                    />
                    <p className={`text-xs font-semibold uppercase tracking-[0.15em] ${metaClass}`}>{d.available ? 'Available' : 'Coming Soon'}</p>
                    <h3 className={`mt-1 text-xl font-extrabold ${titleClass}`}>{d.label}</h3>
                    <p className={`mt-2 text-sm font-semibold ${priceClass}`}>{d.price === 0 ? 'Free Trial' : `Rs ${d.price}`}</p>
                  </label>
                )
              })}
            </div>
          )}
          <div className="flex flex-col gap-2 sm:flex-row">
            {step > 1 && <button type="button" onClick={() => setStep((v) => v - 1)} className="rounded-xl border border-brand-500/60 bg-transparent px-4 py-3 text-sm font-bold text-brand-700 transition hover:bg-brand-100 dark:text-brand-100 dark:hover:bg-brand-500/15">Back</button>}
            {step < 3 ? (
              <button type="button" onClick={() => {
                const validation = validateForStep(step)
                if (validation) {
                  setError(validation)
                  return
                }
                setError('')
                setStep((v) => v + 1)
              }} className="rounded-xl border border-brand-600 bg-brand-600 px-4 py-3 text-sm font-bold text-white transition hover:bg-brand-700 dark:border-brand-400 dark:bg-brand-400 dark:text-[#053423] dark:hover:bg-brand-300">Next Step</button>
            ) : (
              <button type="submit" disabled={submitting} className="rounded-xl border border-brand-600 bg-brand-600 px-4 py-3 text-sm font-bold text-white transition hover:bg-brand-700 disabled:cursor-not-allowed disabled:opacity-65 dark:border-brand-400 dark:bg-brand-400 dark:text-[#053423] dark:hover:bg-brand-300">{submitting ? 'Generating Plan...' : 'Get My Plan'}</button>
            )}
          </div>
        </form>
      </section>

      {result && (
        <section className={`rounded-3xl border p-4 shadow-soft sm:p-6 ${isDark ? 'border-[#2e624d] bg-[#0f2a20]' : 'border-brand-300/40 bg-white/92'}`}>
          <h3 className={`brand-title text-3xl font-extrabold sm:text-4xl ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>Your Personalized Meal Plan</h3>
          <div className="mt-4 grid gap-3 md:grid-cols-2 xl:grid-cols-3">
            {Object.entries(result.meal_plans || {}).map(([mealTime, meals]) => (
              <article key={mealTime} className={`rounded-2xl border p-4 ${isDark ? 'border-[#2f6a53] bg-[#163629]' : 'border-brand-300/45 bg-brand-50'}`}>
                <h4 className={`text-xl font-extrabold ${isDark ? 'text-[#e5fff3]' : 'text-brand-700'}`}>{mealTime}</h4>
                <div className="mt-3 space-y-2">
                  {(Array.isArray(meals) ? meals : [meals]).map((meal, index) => (
                    <div key={`${mealTime}-${index}`} className={`rounded-xl border p-3 text-sm ${isDark ? 'border-[#306c53] bg-[#0f251c]' : 'border-brand-200/60 bg-white'}`}>
                      <p className={`font-bold ${isDark ? 'text-[#e4fff2]' : 'text-brand-800'}`}>{meal.item}</p>
                      <p className={`${isDark ? 'text-[#caecd9]' : 'text-slate-600'}`}>{meal.quantity}</p>
                    </div>
                  ))}
                </div>
              </article>
            ))}
          </div>
          <p className={`mt-4 rounded-xl border px-4 py-3 text-sm font-medium ${isDark ? 'border-[#2f6a53] bg-[#163629] text-[#def8ea]' : 'border-brand-300/45 bg-brand-50 text-slate-700'}`}>
            <strong className={isDark ? 'text-[#f0fff8]' : 'text-brand-700'}>Health Tip:</strong> {result.healthy_tip}
          </p>
          <a
            href={`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent('Hi Meal Genie, I would like to order this meal plan.')}`}
            target="_blank"
            rel="noreferrer"
            className={`mt-4 inline-flex rounded-xl border px-4 py-3 text-sm font-bold transition ${isDark ? 'border-[#66efb6] bg-[#66efb6] text-[#042114] hover:bg-[#7cf2be]' : 'border-brand-600 bg-brand-600 text-white hover:bg-brand-700'}`}
          >
            Order via WhatsApp
          </a>
        </section>
      )}
    </main>
  )
}

function Pricing({ theme }) {
  const isDark = theme === 'dark'
  const pricingPlans = [
    {
      name: 'General Health - Vegetarian',
      features: ['Balanced nutrition', 'Vegetarian meals', 'Weekly variety'],
      prices: ['Breakfast: Rs 130', 'Lunch: Rs 150', 'Snack: Rs 99', 'Dinner: Rs 199'],
    },
    {
      name: 'General Health - Non-Vegetarian',
      features: ['Protein-rich meals', 'Non-vegetarian options', 'Weekly variety'],
      prices: ['Breakfast: Rs 110', 'Lunch/Dinner: Rs 159'],
    },
    {
      name: 'Muscle Gain - Vegetarian',
      features: ['High-protein focus', 'Vegetarian meals', 'Calorie-dense support'],
      prices: ['Breakfast: Rs 110', 'Lunch/Dinner: Rs 159'],
    },
    {
      name: 'Muscle Gain - Non-Vegetarian',
      features: ['High-protein focus', 'Non-vegetarian options', 'Calorie-dense support', 'Snacks add-on: Rs 99'],
      prices: ['Breakfast: Rs 129', 'Lunch/Dinner: Rs 169'],
    },
    {
      name: 'Weight Loss - Vegetarian',
      features: ['Calorie-controlled', 'Vegetarian meals', 'Nutrient-dense portions'],
      prices: ['Breakfast: Rs 99', 'Lunch/Dinner: Rs 149'],
    },
    {
      name: 'Weight Loss - Non-Vegetarian',
      features: ['Calorie-controlled', 'Non-vegetarian options', 'Nutrient-dense portions'],
      prices: ['Breakfast: Rs 110', 'Lunch/Dinner: Rs 159'],
    },
  ]

  return (
    <main className="mt-4 space-y-4">
      <section className={`rounded-3xl border p-5 shadow-soft sm:p-6 ${isDark ? 'border-[#2e624d] bg-[#0f2a20]' : 'border-brand-300/40 bg-white/92'}`}>
        <h2 className={`brand-title text-3xl font-extrabold sm:text-4xl ${isDark ? 'text-[#d5ffec]' : 'text-brand-700'}`}>Choose Your Plan</h2>
        <p className={`mt-2 text-sm sm:text-base ${isDark ? 'text-[#caecd9]' : 'text-slate-700'}`}>
          Flexible meal pricing for subscription-based weekly and monthly routines.
        </p>

        <div className="mt-4 grid gap-3 md:grid-cols-2 xl:grid-cols-3">
          {pricingPlans.map((plan) => (
            <article key={plan.name} className={`rounded-2xl border p-4 ${isDark ? 'border-[#2f6a53] bg-[#163629]' : 'border-brand-200/70 bg-brand-50'}`}>
              <h3 className={`text-lg font-extrabold ${isDark ? 'text-[#e5fff3]' : 'text-brand-800'}`}>{plan.name}</h3>
              <ul className={`mt-3 ml-5 list-disc space-y-1 text-sm ${isDark ? 'text-[#d5f4e4]' : 'text-slate-700'}`}>
                {plan.features.map((feature) => (
                  <li key={feature}>{feature}</li>
                ))}
              </ul>
              <div className={`mt-3 rounded-xl border p-3 ${isDark ? 'border-[#306c53] bg-[#0f251c]' : 'border-brand-200/70 bg-white'}`}>
                {plan.prices.map((priceLine) => (
                  <p key={priceLine} className={`text-sm font-semibold ${isDark ? 'text-[#e8fff4]' : 'text-brand-800'}`}>
                    {priceLine}
                  </p>
                ))}
              </div>
              <NavLink
                to="/plan"
                className={`mt-4 inline-flex rounded-xl border px-4 py-2 text-sm font-bold transition ${isDark ? 'border-[#66efb6] bg-[#66efb6] text-[#032116] hover:bg-[#7ef3c0]' : 'border-brand-600 bg-brand-600 text-white hover:bg-brand-700'}`}
              >
                Get Started
              </NavLink>
            </article>
          ))}
        </div>

        <p className={`mt-4 rounded-xl border px-4 py-3 text-sm ${isDark ? 'border-[#2f6a53] bg-[#163629] text-[#dff9eb]' : 'border-brand-200/70 bg-brand-50 text-slate-700'}`}>
          All prices are per meal box. Custom plan combinations and delivery schedules are available on request.
        </p>
      </section>
    </main>
  )
}

export default App


