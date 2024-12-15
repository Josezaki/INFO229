import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import { Open_Sans, Raleway } from "next/font/google";  // Importa las nuevas fuentes
import "./globals.css";

// Fuentes existentes
const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

// Nuevas fuentes
const openSans = Open_Sans({
  variable: "--font-open-sans",
  subsets: ["latin"],
  weight: ["400", "600"], // Usa 'weight' en lugar de 'weights'
});

const raleway = Raleway({
  variable: "--font-raleway",
  subsets: ["latin"],
  weight: ["400", "700"], // Usa 'weight' en lugar de 'weights'
});

export const metadata: Metadata = {
  title: "Jobbly - Plataforma de servicios",
  description: "Conéctate con estudiantes de la Universidad Austral para solicitar y ofrecer servicios.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <body
        className={`${geistSans.variable} ${geistMono.variable} ${openSans.variable} ${raleway.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
