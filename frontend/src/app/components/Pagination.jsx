import React, { useState, useEffect } from "react";

export default function Pagination({ currentPage, totalPages, onPageChange }) {
  const [clickedButton, setClickedButton] = useState(null); // track last clicked button

  const pages = Array.from({ length: totalPages }, (_, i) => i + 1);

  // Clear clickedButton after 200ms for click effect
  useEffect(() => {
    if (clickedButton !== null) {
      const timer = setTimeout(() => setClickedButton(null), 200);
      return () => clearTimeout(timer);
    }
  }, [clickedButton]);

  // Determine button classes
  const getClass = (pageOrName) => {
    if (clickedButton === pageOrName || currentPage === pageOrName) {
      return "px-3 py-1 rounded-[8px] bg-black text-white";
    }
    return "px-3 py-1 rounded-[8px] bg-[#E6E6E6]";
  };

  return (
    <div className="flex justify-center items-center gap-4 mt-10">
      {/* Prev */}
      <button
        onClick={() => {
          setClickedButton("prev");
          onPageChange(currentPage - 1);
        }}
        disabled={currentPage === 1}
        className={getClass("prev") + " disabled:opacity-50"}
      >
        Prev
      </button>

      {/* Page numbers */}
      {pages.map((page) => (
        <button
          key={page}
          onClick={() => {
            setClickedButton(page);
            onPageChange(page);
          }}
          className={getClass(page)}
        >
          {page}
        </button>
      ))}

      {/* Next */}
      <button
        onClick={() => {
          setClickedButton("next");
          onPageChange(currentPage + 1);
        }}
        disabled={currentPage === totalPages}
        className={getClass("next") + " disabled:opacity-50"}
      >
        Next
      </button>
    </div>
  );
}

