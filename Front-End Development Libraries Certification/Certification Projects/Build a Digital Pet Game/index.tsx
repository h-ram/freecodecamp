const { useState, useEffect, useRef } = React;

export enum PetMood {
  HAPPY,
  EXCITED,
  CONTENT,
  SAD,
  TIRED,
  SICK,
  HUNGRY
}

enum PetAction {
  EAT,
  PLAY,
  SLEEP
}

// Joins the lines of an ASCII drawing. Backslashes are doubled because this is a normal string.
const art = (...lines: string[]): string => lines.join('\n');

const moodArt: Record<PetMood, string> = {
  [PetMood.HAPPY]: art(
    ' /\\_/\\',
    '( ^.^ )',
    ' > w <',
    ' /|_|\\'
  ),
  [PetMood.EXCITED]: art(
    '*/\\_/\\*',
    '( ^o^ )',
    ' > W <',
    ' \\|_|/'
  ),
  [PetMood.CONTENT]: art(
    ' /\\_/\\',
    '( o.o )',
    ' > - <',
    ' /|_|\\'
  ),
  [PetMood.SAD]: art(
    ' /\\_/\\',
    '( T.T )',
    ' > n <',
    '  |_|'
  ),
  [PetMood.TIRED]: art(
    ' /\\_/\\  z',
    '( -.- )  Z',
    ' > _ <',
    '  |_|'
  ),
  [PetMood.SICK]: art(
    ' /\\_/\\  +',
    '( x.x )',
    ' > ~ <',
    '  |_|'
  ),
  [PetMood.HUNGRY]: art(
    ' /\\_/\\',
    '( o.o )',
    ' > O <',
    ' \\___/'
  )
};

const moodLabel: Record<PetMood, string> = {
  [PetMood.HAPPY]: 'HAPPY',
  [PetMood.EXCITED]: 'EXCITED',
  [PetMood.CONTENT]: 'CONTENT',
  [PetMood.SAD]: 'SAD',
  [PetMood.TIRED]: 'TIRED',
  [PetMood.SICK]: 'SICK',
  [PetMood.HUNGRY]: 'HUNGRY'
};

const TICK_MS = 10000;
const TICK_HUNGER = 3;
const TICK_HAPPINESS = 2;
const BAR_SEGMENTS = 10;

const clamp = (value: number): number => Math.max(0, Math.min(100, value));

const getMood = (hunger: number, happiness: number, energy: number): PetMood => {
  if (hunger > 70) return PetMood.HUNGRY;
  if (energy < 30) return PetMood.TIRED;
  if (happiness < 30) return PetMood.SAD;
  if (happiness > 80 && energy > 70) return PetMood.EXCITED;
  if (happiness > 60) return PetMood.HAPPY;
  return PetMood.CONTENT;
};

// Text meter such as [######....]. A trailing "!" warns that the value is in a bad zone.
const asciiBar = (value: number, highIsBad: boolean): string => {
  const filled = Math.round((value / 100) * BAR_SEGMENTS);
  const bar = '#'.repeat(filled) + '.'.repeat(BAR_SEGMENTS - filled);
  const goodness = highIsBad ? 100 - value : value;
  return '[' + bar + ']' + (goodness < 30 ? '!' : ' ');
};

export const PetGame = () => {
  const [started, setStarted] = useState(false);
  const [petName, setPetName] = useState('');
  const [formError, setFormError] = useState('');

  const [hunger, setHunger] = useState(0);
  const [happiness, setHappiness] = useState(100);
  const [energy, setEnergy] = useState(100);

  const nameRef = useRef<HTMLInputElement>(null);

  // While the game is running, the pet slowly gets hungrier and lonelier.
  useEffect(() => {
    if (!started) return;

    const id = setInterval(() => {
      setHunger((h) => clamp(h + TICK_HUNGER));
      setHappiness((h) => clamp(h - TICK_HAPPINESS));
    }, TICK_MS);

    return () => clearInterval(id);
  }, [started]);

  const handleStart = (e: React.MouseEvent) => {
    e.preventDefault();
    const name = (nameRef.current ? nameRef.current.value : '').trim();

    if (!name) {
      setFormError('ERROR: a pet needs a name.');
      return;
    }

    setPetName(name);
    setFormError('');
    setStarted(true);
  };

  const doAction = (action: PetAction): void => {
    switch (action) {
      case PetAction.EAT:
        setHunger((h) => clamp(h - 15));
        setEnergy((n) => clamp(n + 5));
        break;
      case PetAction.PLAY:
        setEnergy((n) => clamp(n - 10));
        setHappiness((h) => clamp(h + 10));
        break;
      case PetAction.SLEEP:
        setHunger((h) => clamp(h + 10));
        setEnergy((n) => clamp(n + 20));
        break;
    }
  };

  const mood = getMood(hunger, happiness, energy);

  return (
    <main className="device">
      <h1 className="brand">== POCKET PET ==</h1>

      <section className="screen">
        {!started ? (
          <form className="hatch" onSubmit={(e) => e.preventDefault()}>
            <label htmlFor="pet-name">&gt; NAME YOUR PET_</label>
            <input
              id="pet-name"
              name="pet-name"
              type="text"
              maxLength={20}
              autoComplete="off"
              ref={nameRef}
            />
            <p className="form-error" role="alert">{formError}</p>
            <button type="submit" className="start" onClick={handleStart}>
              [ HATCH ]
            </button>
          </form>
        ) : (
          <div className="play-area">
            <pre className="pet-face" aria-label={'Pet is ' + moodLabel[mood].toLowerCase()}>
              {moodArt[mood]}
            </pre>
            <h2 className="pet-name">{petName}</h2>
            <p className="pet-mood" aria-live="polite">[ MOOD: {moodLabel[mood]} ]</p>

            <div className="stats">
              <div className="stat">
                <span className="stat-label">Hunger</span>
                <span className="stat-meter" aria-hidden="true">{asciiBar(hunger, true)}</span>
                <span className="stat-value">{hunger}</span>
              </div>

              <div className="stat">
                <span className="stat-label">Happiness</span>
                <span className="stat-meter" aria-hidden="true">{asciiBar(happiness, false)}</span>
                <span className="stat-value">{happiness}</span>
              </div>

              <div className="stat">
                <span className="stat-label">Energy</span>
                <span className="stat-meter" aria-hidden="true">{asciiBar(energy, false)}</span>
                <span className="stat-value">{energy}</span>
              </div>
            </div>
          </div>
        )}
      </section>

      {started && (
        <div className="controls">
          <button id="eat-action" className="action" onClick={() => doAction(PetAction.EAT)}>
            [ EAT ]
          </button>
          <button id="play-action" className="action" onClick={() => doAction(PetAction.PLAY)}>
            [ PLAY ]
          </button>
          <button id="sleep-action" className="action" onClick={() => doAction(PetAction.SLEEP)}>
            [ SLEEP ]
          </button>
        </div>
      )}
    </main>
  );
};