export default function Header() {
  return (
    <header className="w-full h-[148px] bg-[#92BA8E]">
      <div className="w-full h-[148px] bg-[#92BA8E] flex items-center justify-between px-[80px]">

        {/* Left: Logo */}
        <div
          className="text-white"
          style={{
            fontFamily: "var(--font-roboto)",
            fontSize: "45px",
            fontWeight: 400,
          }}
        >
          Electronics
        </div>

        {/* Right: Menu */}
        <nav className="flex gap-[48px]">
          <a
            href="#"
            className="text-white"
            style={{
              fontFamily: "var(--font-inter)",
              fontSize: "20px",
              fontWeight: 500,
            }}
          >
            Home
          </a>
          <a
            href="#"
            className="text-white"
            style={{
              fontFamily: "var(--font-inter)",
              fontSize: "20px",
              fontWeight: 500,
            }}
          >
            About Us
          </a>
          <a
            href="#"
            className="text-white"
            style={{
              fontFamily: "var(--font-inter)",
              fontSize: "20px",
              fontWeight: 500,
            }}
          >
            Contacts
          </a>
          <a
            href="#"
            className="text-white"
            style={{
              fontFamily: "var(--font-inter)",
              fontSize: "20px",
              fontWeight: 500,
            }}
          >
            Login
          </a>
          <button
            className="bg-black text-white px-5 py-2 rounded-[8px]"
            style={{
              fontFamily: "var(--font-inter)",
              fontSize: "16px",
              fontWeight: 500,
            }}
          >
            CART
          </button>
        </nav>
      </div>
    </header>
  );
}