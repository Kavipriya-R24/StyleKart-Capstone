import streamlit as st
from google import genai
import mysql.connector
import pandas as pd

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="StyleKart AI Analytics",
    page_icon="🛍️",
    layout="wide"
)

# =========================================================
# CUSTOM UI STYLE
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.title {
    font-size: 42px;
    font-weight: 700;
    color: #20346B;
    margin-bottom: 0px;
}

.subtitle {
    font-size: 18px;
    color: #555;
    margin-bottom: 25px;
}

.section-title {
    font-size: 24px;
    font-weight: 650;
    color: #20346B;
    margin-top: 25px;
    margin-bottom: 10px;
}

.success-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #eaf8f0;
    border: 1px solid #9bd5b5;
    color: #17663a;
    font-weight: 600;
}

.info-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #eef7fb;
    border: 1px solid #8fd5ea;
    color: #20346B;
}

.insight-box {
    padding: 20px;
    border-radius: 12px;
    background-color: white;
    border-left: 5px solid #24BAEC;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    line-height: 1.6;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">🛍️ StyleKart AI Analytics Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Natural-Language-to-SQL & AI-Assisted Business Insights'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# GEMINI CLIENT
# =========================================================

try:
    client = genai.Client()
except Exception as e:
    st.error("Gemini client could not be initialized.")
    st.stop()


# =========================================================
# MYSQL CONNECTION
# =========================================================

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="stylekart_capstone"
    )

    cursor = db.cursor()

except Exception as e:
    st.error(f"MySQL connection failed: {e}")
    st.stop()


# =========================================================
# DATABASE SCHEMA
# =========================================================

schema = """
Database: stylekart_capstone

Tables:

Customers:
Customer_ID, Customer_Name, Age, Gender, City, State,
Region, Customer_Segment, Registration_Date

Products:
Product_ID, Product_Name, Category, Brand, Price

Orders:
Order_ID, Customer_ID, Product_ID, Order_Date,
Quantity, Order_Amount, Order_Status

Payments:
Payment_ID, Order_ID, Payment_Method,
Payment_Status, Amount

Returns:
Return_ID, Order_ID, Product_ID, Return_Reason,
Return_Quantity, Refund_Amount

Inventory:
Inventory_ID, Last_Updated, Product_ID,
Reorder_Level, Stock_Quantity, Warehouse
"""


# =========================================================
# QUESTION INPUT
# =========================================================

st.markdown(
    '<div class="section-title">1. Ask a Business Question</div>',
    unsafe_allow_html=True
)

question = st.text_area(
    "Enter your question:",
    value="Which product categories generated the highest revenue?",
    height=100,
    placeholder="Example: Which region generated the highest revenue?"
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

analyze_button = st.button(
    "🚀 Generate SQL & Insight",
    type="primary",
    use_container_width=True
)


# =========================================================
# MAIN ANALYSIS
# =========================================================

if analyze_button:

    if not question.strip():
        st.warning("Please enter a business question.")
        st.stop()

    # -----------------------------------------------------
    # GENERATE SQL
    # -----------------------------------------------------

    with st.spinner("Gemini is generating SQL..."):

        prompt = f"""
You are a SQL analyst working with the StyleKart
fashion e-commerce database.

Database schema:
{schema}

Business question:
{question}

Generate a MySQL query that answers the business question.

Rules:
- Use only the tables and columns provided in the schema.
- Do not invent columns.
- Use correct JOIN conditions.
- Use appropriate aggregation.
- Sort the result when ranking is requested.
- Return only the SQL query.
"""

        try:

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

            generated_sql = response.text.strip()

            # Remove Markdown code fences
            generated_sql = generated_sql.replace("```sql", "")
            generated_sql = generated_sql.replace("```", "")
            generated_sql = generated_sql.strip()

        except Exception as e:
            st.error(f"Gemini SQL generation failed: {e}")
            st.stop()


    # -----------------------------------------------------
    # DISPLAY GENERATED SQL
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">2. Generated SQL</div>',
        unsafe_allow_html=True
    )

    st.code(
        generated_sql,
        language="sql"
    )


    # -----------------------------------------------------
    # BASIC SAFETY CHECK
    # -----------------------------------------------------

    sql_lower = generated_sql.lower().strip()

    if not sql_lower.startswith("select"):
        st.error(
            "The generated query was not a SELECT statement. "
            "Execution was stopped for safety."
        )
        st.stop()


    # -----------------------------------------------------
    # EXECUTE SQL
    # -----------------------------------------------------

    with st.spinner("Executing SQL query..."):

        try:

            cursor.execute(generated_sql)

            rows = cursor.fetchall()

            columns = [desc[0] for desc in cursor.description]

            result_df = pd.DataFrame(
                rows,
                columns=columns
            )

        except Exception as e:
            st.error(f"SQL execution failed: {e}")
            st.stop()


    # -----------------------------------------------------
    # QUERY RESULT
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">3. Query Result</div>',
        unsafe_allow_html=True
    )

    if result_df.empty:

        st.warning("The query returned no results.")

    else:

        st.dataframe(
            result_df,
            use_container_width=True,
            hide_index=True
        )


    # -----------------------------------------------------
    # SUCCESS STATUS
    # -----------------------------------------------------

    st.markdown(
        """
        <div class="success-box">
        ✓ SQL Generated Successfully &nbsp;&nbsp;
        ✓ SQL Executed Successfully &nbsp;&nbsp;
        ✓ Result Retrieved from MySQL
        </div>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # VERIFIED RESULT
    # -----------------------------------------------------

    verified_result = "\n".join(
        [f"{row[0]}: {row[1]}" for row in rows]
    )


    # -----------------------------------------------------
    # AI INSIGHT
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">4. AI-Assisted Business Insight</div>',
        unsafe_allow_html=True
    )

    insight_prompt = f"""
You are helping prepare a business insights report
for StyleKart Fashion E-Commerce & Retail.

Below is a verified analytical result retrieved
from the StyleKart MySQL database.

{verified_result}

Convert this result into a concise business insight.

Rules:
- Do not invent numbers.
- Do not change any values.
- State the observed pattern objectively.
- Clearly distinguish facts from possible interpretations.
- Do not claim causation unless supported by the data.
- Explain why the finding may matter to StyleKart.
"""

    with st.spinner("Generating business insight..."):

        try:

            insight_response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=insight_prompt
            )

            insight = insight_response.text.strip()

        except Exception as e:
            st.error(f"Insight generation failed: {e}")
            st.stop()


    st.markdown(
        f"""
        <div class="insight-box">
        <strong>AI-Assisted Insight</strong>
        <br><br>
        {insight}
        </div>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # VALIDATION INFORMATION
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">5. Analysis Status</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("✓ Gemini SQL Generated")

    with col2:
        st.success("✓ MySQL Query Executed")

    with col3:
        st.success("✓ Result Retrieved")


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "StyleKart Analytics Capstone | "
    "Natural-Language-to-SQL + AI-Assisted Insights"
)