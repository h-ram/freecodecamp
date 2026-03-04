const form = document.getElementById("form");
const fullName = document.getElementById("full-name");
const email = document.getElementById("email");
const orderNo = document.getElementById("order-no");
const productCode = document.getElementById("product-code");
const quantity = document.getElementById("quantity");
const complaintsGroup = document.getElementById("complaints-group");
const complaintDescription = document.getElementById("complaint-description");
const solutionsGroup = document.getElementById("solutions-group");
const solutionDescription = document.getElementById("solution-description");

function validateForm() {
  const fullNameValid = fullName.value.trim() !== "";
  const emailValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value);
  const orderNoValid = /^2024\d{6}$/.test(orderNo.value);
  const productCodeValid =
    /^[A-Za-z]{2}\d{2}-[A-Za-z]\d{3}-[A-Za-z]{2}\d$/.test(productCode.value);
  const quantityValid =
    Number.isInteger(+quantity.value) && +quantity.value > 0;
  const checkedComplaints = complaintsGroup.querySelectorAll(
    "input[type='checkbox']:checked",
  );
  const complaintsValid = checkedComplaints.length > 0;
  const otherComplaintChecked =
    document.getElementById("other-complaint").checked;
  const complaintDescriptionValid =
    !otherComplaintChecked || complaintDescription.value.trim().length >= 20;
  const selectedSolution = solutionsGroup.querySelector(
    "input[type='radio']:checked",
  );
  const solutionsValid = !!selectedSolution;
  const otherSolutionChecked =
    document.getElementById("other-solution").checked;
  const solutionDescriptionValid =
    !otherSolutionChecked || solutionDescription.value.trim().length >= 20;

  return {
    "full-name": fullNameValid,
    email: emailValid,
    "order-no": orderNoValid,
    "product-code": productCodeValid,
    quantity: quantityValid,
    "complaints-group": complaintsValid,
    "complaint-description": complaintDescriptionValid,
    "solutions-group": solutionsValid,
    "solution-description": solutionDescriptionValid,
  };
}

function isValid(validationObject) {
  return Object.values(validationObject).every((value) => value === true);
}

function setFieldState(element, valid) {
  if (valid) {
    element.style.borderColor = "green";
  } else {
    element.style.borderColor = "red";
  }
}

function handleChange() {
  const results = validateForm();

  setFieldState(fullName, results["full-name"]);
  setFieldState(email, results.email);
  setFieldState(orderNo, results["order-no"]);
  setFieldState(productCode, results["product-code"]);
  setFieldState(quantity, results.quantity);

  setFieldState(complaintsGroup, results["complaints-group"]);
  setFieldState(complaintDescription, results["complaint-description"]);

  setFieldState(solutionsGroup, results["solutions-group"]);
  setFieldState(solutionDescription, results["solution-description"]);
}

form.addEventListener("change", handleChange);

form.addEventListener("submit", function (e) {
  e.preventDefault();

  const results = validateForm();

  if (!isValid(results)) {
    handleChange();
    return;
  }

  document.getElementById("message-box").textContent =
    "Form submitted successfully.";
});
