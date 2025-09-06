import { Button } from '@/components/ui/button';
import { cn } from '@/lib/utils';

interface WelcomeProps {
  disabled: boolean;
  startButtonText: string;
  onStartCall: () => void;
}

export const Welcome = ({
  disabled,
  startButtonText,
  onStartCall,
  ref,
}: React.ComponentProps<'div'> & WelcomeProps) => {
  return (
    <section
      ref={ref}
      inert={disabled}
      className={cn(
        'bg-background scanlines fixed inset-0 mx-auto flex h-svh flex-col items-center justify-center text-center',
        disabled ? 'z-10' : 'z-20'
      )}
    >
      <div className="recording-dot"></div>
      <svg
        width="64"
        height="64"
        viewBox="0 0 64 64"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        className="text-fg0 mb-4 size-16"
      >
        <path
          d="M32 10C18.7 10 7.8 18.9 2 32c5.8 13.1 16.7 22 30 22s24.2-8.9 30-22C56.2 18.9 45.3 10 32 10zm0 36c-7.7 0-14-6.3-14-14s6.3-14 14-14 14 6.3 14 14-6.3 14-14 14z"
          fill="currentColor"
        />
        <circle cx="32" cy="32" r="8" fill="#ff0033" />
      </svg>

      <h1
        className="text-fg0 glitch mb-2 max-w-prose pt-1 text-xl leading-7 font-bold"
        data-text="THEY'RE WATCHING YOUR EVERY TRANSACTION"
      >
        THEY'RE WATCHING YOUR EVERY TRANSACTION
      </h1>
      <p className="text-fg1 max-w-prose pt-1 text-sm leading-6 font-medium">
        Learn what the IRS doesn't want you to know
      </p>
      <Button variant="primary" size="lg" onClick={onStartCall} className="mt-6 w-64 font-mono">
        {startButtonText}
      </Button>
      <footer className="fixed bottom-5 left-0 z-20 flex w-full items-center justify-center">
        <p className="text-fg3 scanlines max-w-prose pt-1 text-xs leading-5 font-normal text-pretty md:text-sm">
          <span className="text-fgSerious font-mono">CLASSIFIED LEVEL 7</span> • THIS CONVERSATION
          IS BEING MONITORED
        </p>
      </footer>
    </section>
  );
};
