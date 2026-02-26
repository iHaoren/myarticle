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
            <div>
                
            </div>
        </header>
    )