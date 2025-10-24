import type { AppProps } from 'next/app';
import Head from 'next/head';
import '../styles/globals.css';  // This imports Tailwind styles

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>Business Idea Generator</title>
      </Head>
      <Component {...pageProps} />
    </>
  );
}