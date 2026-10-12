import http.server
import socketserver

PORT = 8000

HTML = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coccole - Studio di Manicure & Estetica</title>
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Syne:wght@500;700;800&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --bg-hero: #0F0A0C;
            --primary: #E28B9F;
            --primary-glow: rgba(226, 139, 159, 0.35);
            --accent: #F1C3AD;
            --bg-body: #FAF7F6;
            --bg-card: #FFFFFF;
            --text-main: #1D191A;
            --text-muted: #6E696B;
            --text-light: #ECE6E8;
            --radius-xl: 32px;
            --radius-lg: 20px;
            --radius-sm: 12px;
            --shadow-soft: 0 20px 40px rgba(0, 0, 0, 0.04);
            --shadow-hover: 0 25px 50px rgba(226, 139, 159, 0.15);
            --insta-gradient: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
        }

        html {
            scroll-behavior: smooth;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-body);
            color: var(--text-main);
            font-family: 'Plus Jakarta Sans', sans-serif;
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
            overflow-x: hidden;
        }

        h1, h2, h3, .brand-font {
            font-family: 'Syne', sans-serif;
        }

        /* NAVBAR */
        nav {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            padding: 2rem 3rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 100;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 800;
            color: #FFFFFF;
            letter-spacing: -0.5px;
            text-decoration: none;
        }

        .logo span {
            color: var(--primary);
        }

        .nav-links {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .nav-social {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 8px 18px;
            border-radius: 50px;
            color: var(--text-light);
            font-size: 0.85rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s ease;
        }

        .nav-social:hover {
            background: rgba(255, 255, 255, 0.18);
            border-color: rgba(255, 255, 255, 0.3);
            transform: translateY(-2px);
        }

        /* HERO SECTION */
        .hero {
            background-color: var(--bg-hero);
            min-height: 90vh;
            padding: 9rem 2rem 5rem;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            overflow: hidden;
        }

        .glow-1 {
            position: absolute;
            top: -10%;
            left: 15%;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(226, 139, 159, 0.35) 0%, rgba(0,0,0,0) 70%);
            filter: blur(70px);
            pointer-events: none;
        }

        .glow-2 {
            position: absolute;
            bottom: -10%;
            right: 10%;
            width: 550px;
            height: 550px;
            background: radial-gradient(circle, rgba(241, 195, 173, 0.25) 0%, rgba(0,0,0,0) 70%);
            filter: blur(90px);
            pointer-events: none;
        }

        .hero-container {
            max-width: 1200px;
            width: 100%;
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 4rem;
            align-items: center;
            position: relative;
            z-index: 2;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(226, 139, 159, 0.12);
            border: 1px solid rgba(226, 139, 159, 0.3);
            color: var(--primary);
            padding: 8px 18px;
            border-radius: 50px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .hero-badge-dot {
            width: 8px;
            height: 8px;
            background-color: var(--primary);
            border-radius: 50%;
            box-shadow: 0 0 10px var(--primary);
        }

        .hero h1 {
            font-size: 4.2rem;
            line-height: 1.05;
            font-weight: 800;
            letter-spacing: -1.5px;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, #FFFFFF 0%, #E6D8DC 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero h1 i {
            font-style: italic;
            font-weight: 500;
            color: var(--primary);
            -webkit-text-fill-color: var(--primary);
        }

        .hero p {
            font-size: 1.2rem;
            color: #A39B9E;
            margin-bottom: 2.5rem;
            max-width: 540px;
            font-weight: 300;
        }

        .hero-actions {
            display: flex;
            gap: 1.2rem;
            align-items: center;
            flex-wrap: wrap;
        }

        .btn-primary {
            background: var(--primary);
            color: #120c0e;
            padding: 1.1rem 2.4rem;
            border-radius: 50px;
            font-weight: 700;
            text-decoration: none;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 10px 25px var(--primary-glow);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            background: #eab0bd;
            box-shadow: 0 15px 30px var(--primary-glow);
        }

        .btn-instagram {
            background: var(--insta-gradient);
            color: white;
            padding: 1.1rem 2rem;
            border-radius: 50px;
            font-weight: 600;
            text-decoration: none;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 10px 25px rgba(220, 39, 67, 0.25);
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }

        .btn-instagram:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(220, 39, 67, 0.4);
        }

        /* CARD HERO VISUALE MODERNA */
        .hero-card {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(25px);
            padding: 2.5rem;
            border-radius: var(--radius-xl);
            box-shadow: 0 30px 60px rgba(0,0,0,0.5);
        }

        .hero-card-header {
            display: flex;
            align-items: center;
            gap: 1.2rem;
            margin-bottom: 2rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }

        .hero-card-avatar {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 1.4rem;
            color: #120c0e;
        }

        .hero-card-info h4 {
            font-size: 1.3rem;
            color: white;
            font-weight: 700;
        }

        .hero-card-info p {
            font-size: 0.9rem;
            color: #A39B9E;
            margin-bottom: 0;
        }

        .hero-stats {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
        }

        .stat-box {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.06);
            padding: 1.2rem;
            border-radius: var(--radius-lg);
        }

        .stat-number {
            font-size: 1.4rem;
            font-weight: 800;
            color: var(--primary);
            font-family: 'Syne', sans-serif;
        }

        .stat-label {
            font-size: 0.85rem;
            color: #A39B9E;
        }

        /* LAYOUT CONTENUTO */
        .container {
            max-width: 1100px;
            margin: 4rem auto;
            padding: 0 2rem;
        }

        .section {
            background: var(--bg-card);
            padding: 3.5rem;
            border-radius: var(--radius-xl);
            box-shadow: var(--shadow-soft);
            margin-bottom: 3rem;
            border: 1px solid rgba(0, 0, 0, 0.03);
        }

        .section-title {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            letter-spacing: -0.5px;
        }

        .section-sub {
            color: var(--text-muted);
            margin-bottom: 2.5rem;
        }

        /* TEAM GRID */
        .team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .team-card {
            background: #FAF7F6;
            border: 1px solid #EFE8E9;
            padding: 2.2rem;
            border-radius: var(--radius-lg);
            transition: all 0.3s ease;
        }

        .team-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05);
            border-color: var(--primary);
        }

        .team-name {
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--text-main);
        }

        .team-role {
            display: inline-block;
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--primary);
            margin-top: 0.3rem;
            margin-bottom: 1rem;
        }

        .contact-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-top: 1.2rem;
            padding: 0.7rem 1.4rem;
            background: #25D366;
            color: white;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            transition: background 0.2s ease;
        }

        .contact-link:hover {
            background: #1DA851;
        }

        /* LISTINO PREZZI MODERNO */
        .price-category {
            margin-bottom: 3rem;
        }

        .price-category:last-child {
            margin-bottom: 0;
        }

        .category-title {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid var(--primary);
        }

        .category-icon {
            background: rgba(226, 139, 159, 0.15);
            padding: 6px 12px;
            border-radius: var(--radius-sm);
            font-size: 1.2rem;
        }

        .services-list {
            list-style: none;
            display: grid;
            gap: 1.2rem;
        }

        .service-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 1.2rem;
            background: #FAF7F6;
            border-radius: var(--radius-lg);
            border: 1px solid #EFE8E9;
            transition: all 0.2s ease;
        }

        .service-item:hover {
            border-color: var(--primary);
            background: #FFF;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.03);
        }

        .service-title {
            font-weight: 600;
            font-size: 1.05rem;
            color: var(--text-main);
        }

        .service-price {
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-main);
            background: #FAF0F2;
            color: #C05872;
            padding: 6px 16px;
            border-radius: 50px;
            white-space: nowrap;
        }

        /* BANNER INSTAGRAM INTEGRATO */
        .insta-banner {
            background: linear-gradient(135deg, #120c0e 0%, #1a1014 100%);
            color: white;
            border-radius: var(--radius-xl);
            padding: 3.5rem;
            text-align: center;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(226, 139, 159, 0.2);
        }

        .insta-banner h2 {
            font-size: 2.4rem;
            margin-bottom: 0.8rem;
        }

        .insta-banner p {
            color: #A39B9E;
            font-size: 1.1rem;
            margin-bottom: 2rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        /* CONTACT SECTION */
        .contact-box {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-top: 1.5rem;
        }

        .contact-card-item {
            background: #FAF7F6;
            padding: 2rem;
            border-radius: var(--radius-lg);
            text-align: center;
            border: 1px solid #EFE8E9;
        }

        .contact-card-item h3 {
            font-size: 1.4rem;
            margin-bottom: 0.5rem;
        }

        .contact-card-item p {
            color: var(--text-muted);
            margin-bottom: 1.2rem;
        }

        .phone-link {
            color: var(--text-main);
            text-decoration: none;
            font-weight: 600;
        }

        .phone-link:hover {
            color: var(--primary);
        }

        .email-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-top: 1.5rem;
            padding: 1rem 1.8rem;
            background: #FAF7F6;
            border: 1px solid #EFE8E9;
            border-radius: 50px;
            color: var(--text-main);
            text-decoration: none;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .email-badge:hover {
            border-color: var(--primary);
            color: var(--primary);
            transform: translateY(-2px);
        }

        footer {
            text-align: center;
            padding: 3rem;
            color: var(--text-muted);
            font-size: 0.9rem;
        }

        footer a {
            color: inherit;
            text-decoration: underline;
        }

        @media (max-width: 900px) {
            .hero-container { grid-template-columns: 1fr; text-align: center; gap: 3rem; }
            .hero h1 { font-size: 3rem; }
            .hero p { margin-left: auto; margin-right: auto; }
            .hero-actions { justify-content: center; }
            nav { padding: 1.5rem; flex-direction: column; gap: 1rem; }
            .section { padding: 2rem; }
            .insta-banner { padding: 2.5rem 1.5rem; }
        }
    </style>
</head>
<body>

    <nav>
        <a href="#" class="logo brand-font">COCCOLE<span>.</span></a>
        <div class="nav-links">
            <a href="mailto:coccoledm@gmail.com" class="nav-social">
                ✉️ coccoledm@gmail.com
            </a>
            <a href="https://www.instagram.com/coccole.18/" target="_blank" class="nav-social">
                📸 @coccole.18
            </a>
        </div>
    </nav>

    <!-- HERO SECTION MODERNA -->
    <section class="hero">
        <div class="glow-1"></div>
        <div class="glow-2"></div>

        <div class="hero-container">
            <div>
                <div class="hero-badge">
                    <span class="hero-badge-dot"></span>
                    Mihaela & Dorina
                </div>
                <h1 class="brand-font">L'arte delle mani e dei piedi, <i>in famiglia.</i></h1>
                <p>Un’esperienza di bellezza e benessere firmata Mihaela e Dorina. Passione, cura per il dettaglio e trattamenti esclusivi per te.</p>
                <div class="hero-actions">
                    <a href="#prenota" class="btn-primary">Prenota Appuntamento</a>
                    <a href="https://www.instagram.com/coccole.18/" target="_blank" class="btn-instagram">
                        Seguici su Instagram
                    </a>
                </div>
            </div>

            <div class="hero-card">
                <div class="hero-card-header">
                    <div class="hero-card-avatar">C</div>
                    <div class="hero-card-info">
                        <h4>Studio Coccole</h4>
                        <p>@coccole.18</p>
                    </div>
                </div>
                <div class="hero-stats">
                    <div class="stat-box">
                        <div class="stat-number">Mihaela</div>
                        <div class="stat-label">Manicure & Cura Naturale</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">Dorina</div>
                        <div class="stat-label">Nail Art & Gel</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <div class="container">
        
        <!-- CHI SIAMO -->
        <div class="section">
            <h2 class="section-title brand-font">Chi Siamo</h2>
            <p class="section-sub">Due generazioni unite dalla passione per il benessere e la bellezza delle tue mani e dei tuoi piedi.</p>

            <div class="team-grid">
                <div class="team-card">
                    <div class="team-name">Mihaela</div>
                    <span class="team-role">Manicure Classica & Cura Naturale</span>
                    <p style="color: var(--text-muted); font-size: 0.95rem;">
                        Specializzata nella cura profonda dell'unghia naturale, manicure russa, pedicure curativo e trattamenti rigeneranti.
                    </p>
                    <a href="https://wa.me/393791470000" target="_blank" class="contact-link">
                        💬 WhatsApp Mihaela
                    </a>
                </div>

                <div class="team-card">
                    <div class="team-name">Dorina</div>
                    <span class="team-role">Nail Art & Ricostruzione Gel</span>
                    <p style="color: var(--text-muted); font-size: 0.95rem;">
                        Esperta in ricostruzioni in gel, copertura, semipermanente ad alta tenuta e decorazioni artistiche personalizzate.
                    </p>
                    <a href="https://wa.me/393791038760" target="_blank" class="contact-link">
                        💬 WhatsApp Dorina
                    </a>
                </div>
            </div>
        </div>

        <!-- LISTINO PREZZI COMPLETO -->
        <div class="section" id="servizi">
            <h2 class="section-title brand-font">Listino Prezzi</h2>
            <p class="section-sub">Trattamenti professionali e trasparenti per mani e piedi impeccabili.</p>

            <!-- SEZIONE MANI -->
            <div class="price-category">
                <div class="category-title brand-font">
                    <span class="category-icon">💅</span> TRATTAMENTI MANI
                </div>
                <ul class="services-list">
                    <li class="service-item">
                        <div class="service-title">Manicure Classica</div>
                        <div class="service-price">€ 15</div>
                    </li>
                    <li class="service-item">
                        <div class="service-title">Semipermanente</div>
                        <div class="service-price">da € 35</div>
                    </li>
                    <li class="service-item">
                        <div class="service-title">Copertura Gel</div>
                        <div class="service-price">da € 40</div>
                    </li>
                    <li class="service-item">
                        <div class="service-title">Ricostruzione</div>
                        <div class="service-price">da € 55</div>
                    </li>
                    <li class="service-item">
                        <div class="service-title">Ricostruzione Onicofagica</div>
                        <div class="service-price">€ 60</div>
                    </li>
                    <li class="service-item">
                        <div class="service-title">Refill Corto (Misura 1)</div>
                        <div class="service-price">€ 40</div>
                    </li>
                    <li class="service-item">
                        <div class="service-title">Refill Standard</div>
                        <div class="service-price">da € 45</div>
                    </li>
                    <li class="service-item">
                        <div class="service-title">Rimozione Semipermanente</div>
                        <div class="service-price">€ 15</div>
                    </li>
                    <li class="service-item">
                        <div class="service-title">Rimozione Gel</div>
                        <div class="service-price">€ 20</div>
                    </li>
                </ul>
            </div>

            <!-- SEZIONE PIEDI -->
            <div class="price-category">
                <div class="category-title brand-font">
                    <span class="category-icon">🦶</span> TRATTAMENTI PIEDI
                </div>
                <ul class="services-list">
                    <li class="service-item">
                        <div class="service-title">Pedicure Classica</div>
                        <div class="service-price">€ 35</div>
                    </li>
                    <li class="service-item">
                        <div class="service-title">Pedicure Curativa</div>
                        <div class="service-price">da € 40</div>
                    </li>
                    <li class="service-item">
                        <div class="service-title">Semipermanente Piedi</div>
                        <div class="service-price">€ 35</div>
                    </li>
                    <li class="service-item">
                        <div class="service-title">Pedicure Classica + Semipermanente</div>
                        <div class="service-price">€ 50</div>
                    </li>
                    <li class="service-item">
                        <div class="service-title">Rimozione Piedi</div>
                        <div class="service-price">€ 10</div>
                    </li>
                </ul>
            </div>

        </div>

        <!-- BANNER INSTAGRAM DEDICATO -->
        <div class="insta-banner">
            <h2 class="brand-font">Scopri i nostri lavori su Instagram</h2>
            <p>Guarda le ultime novità, le Nail Art realizzate e lasciati ispirare per il tuo prossimo trattamento.</p>
            <a href="https://www.instagram.com/coccole.18/" target="_blank" class="btn-instagram">
                Visita @coccole.18
            </a>
        </div>

        <!-- PRENOTAZIONI -->
        <div class="section" id="prenota">
            <h2 class="section-title brand-font" style="text-align: center;">Prenota il tuo Appuntamento</h2>
            <p class="section-sub" style="text-align: center;">Contatta direttamente Mihaela o Dorina per riservare il tuo momento di relax.</p>
            
            <div class="contact-box">
                <div class="contact-card-item">
                    <h3>Contatta Mihaela</h3>
                    <p>📞 <a href="tel:+393791470000" class="phone-link">+39 379 147 0000</a></p>
                    <a href="https://wa.me/393791470000" target="_blank" class="btn-primary" style="display: inline-block; font-size: 0.9rem; padding: 0.8rem 1.6rem;">
                        Scrivi a Mihaela
                    </a>
                </div>

                <div class="contact-card-item">
                    <h3>Contatta Dorina</h3>
                    <p>📞 <a href="tel:+393791038760" class="phone-link">+39 379 103 8760</a></p>
                    <a href="https://wa.me/393791038760" target="_blank" class="btn-primary" style="display: inline-block; font-size: 0.9rem; padding: 0.8rem 1.6rem;">
                        Scrivi a Dorina
                    </a>
                </div>
            </div>

            <div style="text-align: center;">
                <a href="mailto:coccoledm@gmail.com" class="email-badge">
                    ✉️ Oppure scrivici via email: <strong>coccoledm@gmail.com</strong>
                </a>
            </div>
        </div>

    </div>

    <footer>
        <p>&copy; Coccole Studio Manicure — Mihaela & Dorina | <a href="https://www.instagram.com/coccole.18/" target="_blank">@coccole.18</a> | <a href="mailto:coccoledm@gmail.com">coccoledm@gmail.com</a></p>
    </footer>

</body>
</html>
"""

class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))

if __name__ == "__main__":
    print(f"✨ Sito 'Coccole' con Listino Prezzi Mani & Piedi avviato!")
    print(f"👉 Apri il browser su: http://localhost:{PORT}\n")

    with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
        httpd.serve_forever()
