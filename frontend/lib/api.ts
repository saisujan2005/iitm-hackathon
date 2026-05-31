const API_BASE =
  "http://127.0.0.1:8000";

export async function calculateFine(
  payload: any
) {

  const response = await fetch(
    `${API_BASE}/challan/calculate`,
    {
      method: "POST",

      headers: {
        "Content-Type":
          "application/json",
      },

      body: JSON.stringify(payload),
    }
  );

  return response.json();
}