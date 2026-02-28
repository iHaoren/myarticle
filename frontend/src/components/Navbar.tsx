import { useState, useEffect } from "react";
import { Link, useLocation } from "react-router-dom";

export default function Navbar() {
    const [scrolled, setScrolled] = useState(false)
    const [menuOpen, setMenuOpen] = useState(false)
    const location = useLocation()

    // Scroll detection to monitor the scroll position
    useEffect(() => {
        const handleScroll = () => setScrolled(window.scrollY > 20)
        window.addEventListener("scroll", handleScroll)
        return () => window.removeEventListener("scroll", handleScroll)
    }, [])

    // auto close mobile menu whenn move pages
    useEffect(() => {
        setMenuOpen(false)
    }, [location.pathname])

    const navlinks = [
        { to: '/', label: 'Home'},
        { to: '/admin', label: 'Admin'},
    ]

    const isActive = (path: string) => location.pathname === path

    return (
        <header 
        className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? 
        'bg-white/90 backdrop-blur-md shadow-sm border-b border-stone-100' : 'bg-transparent'}`}>
            <div className="max-w-4xl mx-auto px-6 h-16 flex items-center justify-between">
                
                {/* logo artikel/brand */}
                <Link to="/frontend/public/favicon.svg"
                className="font-serif text-xl font-bold tracking-light text-stone-800 hover:text-indigo-700 transition-colors duration-200">
                ashura<span className="text-indigo-600">article</span>
                </Link>

                {/* Desktop navigation */}
                <nav className="hidden sm:flex items-center gap-1">
                    {navLinks.map(({ to, label}) => (
                        <Link
                        key={to}
                        to={to}
                        className={`px-4 py-2 rounded-full text-sm font-medium  transition-all duration-200 ${isActive(to) 'bg-stone-800 text-white'} `}>
                            {label}
                        </Link>
                    ))}
                </nav>

                {/* mobile hamburger button */}
                <div className={`sm:hidden overflow-hidden transition-all duration-300 ${menuOpen ? 'max-h-40 opacity-100 ' : 'max-h-0 opacity-0'}
                bg-white border-b border-stone-100 shadow-sm`}></div>
            </div>
        </header>
    )
}