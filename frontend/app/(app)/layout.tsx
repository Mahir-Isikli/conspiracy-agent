import { headers } from 'next/headers';
import { getAppConfig } from '@/lib/utils';

interface AppLayoutProps {
  children: React.ReactNode;
}

export default async function AppLayout({ children }: AppLayoutProps) {
  const hdrs = await headers();
  const { companyName, logo, logoDark } = await getAppConfig(hdrs);

  return (
    <>
      <header className="fixed top-0 left-0 z-50 hidden w-full flex-row justify-between p-6 md:flex">
        <div className="flex items-center">
          <div className="recording-dot"></div>
          <span className="text-fgSerious font-mono text-xs font-bold tracking-wider uppercase">
            RECORDING
          </span>
        </div>
        <span
          className="text-fg0 glitch font-mono text-xs font-bold tracking-wider uppercase"
          data-text="CLASSIFIED INFORMATION • ACCESS LEVEL 7"
        >
          CLASSIFIED INFORMATION • ACCESS LEVEL 7
        </span>
      </header>
      {children}
    </>
  );
}
