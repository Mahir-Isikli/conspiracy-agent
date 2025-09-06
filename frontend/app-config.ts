import type { AppConfig } from './lib/types';

export const APP_CONFIG_DEFAULTS: AppConfig = {
  companyName: 'Classified',
  pageTitle: 'The Truth They Don\'t Want You to Know',
  pageDescription: 'Uncover the reality of IRS surveillance and financial tracking systems',

  supportsChatInput: true,
  supportsVideoInput: true,
  supportsScreenShare: true,
  isPreConnectBufferEnabled: true,

  logo: '/lk-logo.svg',
  accent: '#00ff41',
  logoDark: '/lk-logo-dark.svg',
  accentDark: '#00cc33',
  startButtonText: 'UNCOVER THE TRUTH',

  agentName: undefined,
};
